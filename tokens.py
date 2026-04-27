from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    RELATE = auto()
    CHUNKS = auto()
    WHERE = auto()
    TO = auto()
    ENTITY = auto()

    IDENTIFIER = auto()
    STRING = auto()

    EQUAL = auto()
    SEMICOLON = auto()

    END = auto()


@dataclass(frozen=True)
class Token:
    type: TokenType
    text: str