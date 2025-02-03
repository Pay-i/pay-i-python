from enum import Enum


class Instruments(Enum):
    ALL = "all"
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    AWS_BEDROCK = "aws.bedrock"
