import json
from pathlib import Path

from lexer import lex
from parser import Parser
from translator import to_relation_job


EXAMPLES_FILE = Path("dsl_examples.txt")


def process_source(source: str, example_number: int) -> None:
    print("=" * 80)
    print(f"Example {example_number}")
    print("=" * 80)
    print(source)
    print()

    try:
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
        print(json.dumps(job, indent=2))

    except ValueError as error:
        print("ERROR:")
        print(error)

    print()


def main() -> None:
    if not EXAMPLES_FILE.exists():
        raise FileNotFoundError(f"Missing examples file: {EXAMPLES_FILE}")

    sources = [
        line.strip()
        for line in EXAMPLES_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    for index, source in enumerate(sources, start=1):
        process_source(source, index)


if __name__ == "__main__":
    main()