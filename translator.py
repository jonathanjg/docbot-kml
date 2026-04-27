from ast_nodes import RelationStatement


def to_qdrant_filter(statement: RelationStatement) -> dict:
    return {
        "must": [
            {
                "key": statement.condition.field,
                "match": {
                    "value": statement.condition.value,
                },
            }
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