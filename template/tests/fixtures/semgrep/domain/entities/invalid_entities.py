"""Fixture: entities without identity-based equality."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ByEveryField:
    identifier: str
    balance: int


@dataclass(frozen=True, eq=False)
class EqualityWithoutHash:
    identifier: str

    def __eq__(self, other: object) -> bool:
        return isinstance(other, EqualityWithoutHash) and self.identifier == other.identifier
