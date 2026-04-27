from lexer import lex


source = 'relate chunks where doc_type = "pdf" to entity "audit";'

tokens = lex(source)

for token in tokens:
    print(token)