from tokens import Token, TokenType


KEYWORDS = {
    "relate": TokenType.RELATE,
    "chunks": TokenType.CHUNKS,
    "where": TokenType.WHERE,
    "to": TokenType.TO,
    "entity": TokenType.ENTITY,
}


def lex(source: str) -> list[Token]:
    tokens: list[Token] = []
    i = 0

    while i < len(source):
        char = source[i]

        if char.isspace():
            i += 1
            continue

        if char.isalpha() or char == "_":
            word = ""

            while i < len(source) and (source[i].isalnum() or source[i] == "_"):
                word += source[i]
                i += 1

            token_type = KEYWORDS.get(word, TokenType.IDENTIFIER)
            tokens.append(Token(token_type, word))
            continue

        if char == '"':
            i += 1
            value = ""

            while i < len(source) and source[i] != '"':
                value += source[i]
                i += 1

            if i >= len(source):
                raise ValueError("Unterminated string")

            i += 1
            tokens.append(Token(TokenType.STRING, value))
            continue

        if char == "=":
            tokens.append(Token(TokenType.EQUAL, char))
            i += 1
            continue

        if char == ";":
            tokens.append(Token(TokenType.SEMICOLON, char))
            i += 1
            continue

        raise ValueError(f"Unexpected character: {char}")

    tokens.append(Token(TokenType.END, ""))
    return tokens