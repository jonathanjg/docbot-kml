from lexer import lex


source = 'relate chunks where metadata.documentation = "increment" to entity "increment_docs";'

tokens = lex(source)

for token in tokens:
    print(token)