"""Fixture: services that only compute."""

from dataclasses import dataclass


def double(value: int) -> int:
    return value * 2


@dataclass(frozen=True)
class Scaler:
    factor: int

    def apply(self, value: int) -> int:
        return value * self.factor
