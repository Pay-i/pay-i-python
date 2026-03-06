$ErrorActionPreference = "Stop"

Set-Location (Join-Path $PSScriptRoot "..")

if ($args.Count -gt 0 -and $args[0] -eq "--fix") {
    Write-Output "==> Running ruff with --fix"
    uv run ruff check . --fix
}
else {
    Write-Output "==> Running ruff"
    uv run ruff check .
}

Write-Output "==> Running pyright"
uv run pyright

Write-Output "==> Running mypy"
uv run mypy .

Write-Output "==> Making sure it imports"
uv run python -c 'import payi'
