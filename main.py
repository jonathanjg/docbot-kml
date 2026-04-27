from lexer import lex
from parser import Parser
from translator import to_relation_job


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

print()
print("=== RELATION JOB ===")
job = to_relation_job(statement)
print(job)