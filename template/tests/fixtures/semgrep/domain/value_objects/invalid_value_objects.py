"""Fixture: value objects that are not immutable."""

from dataclasses import dataclass


@dataclass
class Plain:
    value: int


@dataclass(frozen=False)
class Explicit:
    value: int


@dataclass(eq=True)
class Unrelated:
    value: int


@dataclass(frozen=True)
class HoldsMutableFields:
    items: list[int]
    mapping: dict[str, int]
    unique: set[str]
