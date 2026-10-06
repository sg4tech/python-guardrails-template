"""Fixture: immutable value objects."""

import dataclasses
from dataclasses import dataclass
from enum import StrEnum


class Color(StrEnum):
    RED = "red"


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    tags: tuple[str, ...] = ()

    def moved(self) -> "Point":
        scratch: list[int] = []
        scratch.append(self.x)
        return Point(scratch[0], self.y)


@dataclasses.dataclass(frozen=True, slots=True)
class Slotted:
    value: int
