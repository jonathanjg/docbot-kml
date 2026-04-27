from ast_nodes import RelationStatement


def to_qdrant_filter(statement: RelationStatement) -> dict:
    return {
        "must": [
            {
                "key": condition.field,
                "match": {
                    "value": condition.value,
                },
            }
            for condition in statement.conditions
        ]
    }


def to_relation_job(statement: RelationStatement) -> dict:
    return {
        "action": "create_relation",
        "source": statement.source,
        "filter": to_qdrant_filter(statement),
        "target": {
            "type": "entity",
            "name": statement.target.name,
        },
    }