from dataclasses import dataclass


@dataclass(frozen=True)
class EqualsCondition:
    field: str
    value: str


@dataclass(frozen=True)
class EntityTarget:
    name: str


@dataclass(frozen=True)
class RelationStatement:
    source: str
    condition: EqualsCondition
    target: EntityTarget