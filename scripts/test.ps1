$ErrorActionPreference = "Stop"

Set-Location (Join-Path $PSScriptRoot "..")

function Test-PrismIsRunning {
    foreach ($targetHost in @("127.0.0.1", "localhost")) {
        $client = $null
        try {
            $client = [System.Net.Sockets.TcpClient]::new()
            $connect = $client.BeginConnect($targetHost, 4010, $null, $null)
            if (-not $connect.AsyncWaitHandle.WaitOne(1000, $false)) {
                continue
            }

            $client.EndConnect($connect)
            return $true
        }
        catch {
            continue
        }
        finally {
            if ($client) {
                $client.Dispose()
            }
        }
    }

    return $false
}

function Stop-ServerOnPort {
    param(
        [Parameter(Mandatory = $true)]
        [int]$Port
    )

    $connections = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
    if (-not $connections) {
        return
    }

    $pids = $connections | Select-Object -ExpandProperty OwningProcess -Unique
    foreach ($processId in $pids) {
        Stop-Process -Id $processId -Force -ErrorAction SilentlyContinue
        Write-Output "Stopped $processId."
    }
}

function Get-OpenApiSpecUrl {
    if (-not (Test-Path ".stats.yml")) {
        return $null
    }

    $match = Select-String -Path ".stats.yml" -Pattern "^\s*openapi_spec_url\s*:\s*(\S+)\s*$" | Select-Object -First 1
    if (-not $match) {
        return $null
    }

    $lineMatch = [regex]::Match($match.Line, "^\s*openapi_spec_url\s*:\s*(\S+)\s*$")
    if (-not $lineMatch.Success) {
        return $null
    }

    return $lineMatch.Groups[1].Value
}

function Start-PrismMockDaemon {
    $url = Get-OpenApiSpecUrl
    if ([string]::IsNullOrWhiteSpace($url)) {
        throw "Error: No OpenAPI spec path/url provided or found in .stats.yml"
    }

    Write-Output "==> Starting mock server with URL $url"

    # If the health check failed but the port is still occupied, clean up stale listeners.
    $existingListeners = Get-NetTCPConnection -LocalPort 4010 -State Listen -ErrorAction SilentlyContinue
    if ($existingListeners) {
        Write-Output "Port 4010 is already in use; stopping existing listener(s) before starting Prism."
        Stop-ServerOnPort -Port 4010
        Start-Sleep -Milliseconds 300
    }

    $runId = [guid]::NewGuid().ToString("N")
    $stdoutLog = ".prism.$runId.log"
    $stderrLog = ".prism.$runId.err.log"

    $npmCmd = (Get-Command npm.cmd -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty Source)
    if ([string]::IsNullOrWhiteSpace($npmCmd)) {
        throw "npm.cmd was not found on PATH"
    }

    $process = Start-Process `
        -FilePath $npmCmd `
        -ArgumentList @("exec", "--yes", "--package=@stainless-api/prism-cli@5.15.0", "--", "prism", "mock", $url) `
        -PassThru `
        -WindowStyle Hidden `
        -RedirectStandardOutput $stdoutLog `
        -RedirectStandardError $stderrLog

    Write-Host -NoNewline "Waiting for server"
    $maxWaitMs = 60000
    $intervalMs = 250
    $elapsedMs = 0

    while ($elapsedMs -lt $maxWaitMs) {
        $log = ""
        if (Test-Path $stdoutLog) {
            $log += Get-Content $stdoutLog -Raw
        }
        if (Test-Path $stderrLog) {
            $log += "`n" + (Get-Content $stderrLog -Raw)
        }

        if (Test-PrismIsRunning) {
            break
        }

        if ($log.Length -gt 0) {
            if ($log -match "fatal") {
                Write-Host
                if (Test-Path $stdoutLog) {
                    Get-Content $stdoutLog
                }
                if (Test-Path $stderrLog) {
                    Get-Content $stderrLog
                }
                throw "Prism mock failed to start"
            }
        }

        Write-Host -NoNewline "."
        Start-Sleep -Milliseconds $intervalMs
        $elapsedMs += $intervalMs

        if ($process.HasExited) {
            Write-Host
            if (Test-Path $stdoutLog) {
                Get-Content $stdoutLog
            }
            if (Test-Path $stderrLog) {
                Get-Content $stderrLog
            }
            throw "Prism mock process exited before becoming ready"
        }
    }

    if (-not (Test-PrismIsRunning)) {
        Write-Host
        if (Test-Path $stdoutLog) {
            Get-Content $stdoutLog
        }
        if (Test-Path $stderrLog) {
            Get-Content $stderrLog
        }
        throw "Prism mock did not become ready within $($maxWaitMs / 1000) seconds"
    }

    Write-Host
    return $process
}

$isOverridingApiBaseUrl = -not [string]::IsNullOrWhiteSpace($env:TEST_API_BASE_URL)
$startedMockProcess = $null

try {
    if (-not $isOverridingApiBaseUrl -and -not (Test-PrismIsRunning)) {
        $startedMockProcess = Start-PrismMockDaemon
    }

    if ($isOverridingApiBaseUrl) {
        Write-Host "[OK] Running tests against $($env:TEST_API_BASE_URL)" -ForegroundColor Green
        Write-Host
    }
    elseif (-not (Test-PrismIsRunning)) {
        Write-Host "ERROR: The test suite will not run without a mock Prism server" -ForegroundColor Red
        Write-Host "running against your OpenAPI spec."
        Write-Host
        Write-Host "To run the server, pass in the path or url of your OpenAPI"
        Write-Host "spec to the prism command:"
        Write-Host
        Write-Host "  npm exec --package=@stainless-api/prism-cli@5.15.0 -- prism mock path/to/your.openapi.yml" -ForegroundColor Yellow
        Write-Host
        exit 1
    }
    else {
        Write-Host "[OK] Mock prism server is running with your OpenAPI spec" -ForegroundColor Green
        Write-Host
    }

    $env:DEFER_PYDANTIC_BUILD = "false"

    # Note that we need to specify the patch version here so that uv
    # won't use unstable (alpha, beta, rc) releases for the tests
    $pyVersionMin = ">=3.9.0"
    $pyVersionMax = ">=3.14.0"

    function Invoke-Tests {
        param(
            [string[]]$TestArgs
        )

        Write-Output "==> Running tests with Pydantic v2"
        & uv run --isolated --all-extras pytest @TestArgs

        # Skip Pydantic v1 tests on latest Python (not supported)
        if ($env:UV_PYTHON -ne $pyVersionMax) {
            Write-Output "==> Running tests with Pydantic v1"
            & uv run --isolated --all-extras --group=pydantic-v1 pytest @TestArgs
        }
    }

    if (-not [string]::IsNullOrWhiteSpace($env:UV_PYTHON)) {
        Invoke-Tests -TestArgs $args
    }
    else {
        Write-Output "==> Running tests for Python $pyVersionMin"
        $env:UV_PYTHON = $pyVersionMin
        Invoke-Tests -TestArgs $args

        Write-Output "==> Running tests for Python $pyVersionMax"
        $env:UV_PYTHON = $pyVersionMax
        Invoke-Tests -TestArgs $args
    }
}
finally {
    if ($startedMockProcess -and -not $startedMockProcess.HasExited) {
        Stop-Process -Id $startedMockProcess.Id -Force -ErrorAction SilentlyContinue
        Write-Output "Stopped $($startedMockProcess.Id)."
    }

    if ($startedMockProcess) {
        Stop-ServerOnPort -Port 4010
    }
}
