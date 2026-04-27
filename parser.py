from ast_nodes import EntityTarget, EqualsCondition, RelationStatement
from tokens import Token, TokenType


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.index = 0

    def current(self) -> Token:
        return self.tokens[self.index]

    def consume(self, expected_type: TokenType, message: str) -> Token:
        token = self.current()

        if token.type != expected_type:
            raise ValueError(f"{message}. Found: {token.type.name} ({token.text!r})")

        self.index += 1
        return token

    def parse_equals_condition(self) -> EqualsCondition:
        field = self.consume(TokenType.IDENTIFIER, "Expected field name")
        self.consume(TokenType.EQUAL, "Expected '=' after field name")
        value = self.consume(TokenType.STRING, "Expected string value after '='")

        return EqualsCondition(
            field=field.text,
            value=value.text,
        )

    def parse(self) -> RelationStatement:
        self.consume(TokenType.RELATE, "Expected 'relate'")
        self.consume(TokenType.CHUNKS, "Expected 'chunks' after 'relate'")
        self.consume(TokenType.WHERE, "Expected 'where' after source")

        conditions = [self.parse_equals_condition()]

        while self.current().type == TokenType.AND:
            self.consume(TokenType.AND, "Expected 'and'")
            conditions.append(self.parse_equals_condition())

        self.consume(TokenType.TO, "Expected 'to' after condition")
        self.consume(TokenType.ENTITY, "Expected 'entity' after 'to'")
        entity_name = self.consume(TokenType.STRING, "Expected entity name after 'entity'")

        self.consume(TokenType.SEMICOLON, "Expected ';' after statement")
        self.consume(TokenType.END, "Expected end of input after ';'")

        return RelationStatement(
            source="chunks",
            conditions=conditions,
            target=EntityTarget(
                name=entity_name.text,
            ),
        )