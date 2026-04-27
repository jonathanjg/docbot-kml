from lexer import lex
from parser import Parser


source = 'relate chunks where metadata.documentation = "increment" to entity "increment_docs";'

tokens = lex(source)

print("=== TOKENS ===")
for token in tokens:
    print(token)

print()
print("=== AST ===")
parser = Parser(tokens)
statement = parser.parse()
print(statement)