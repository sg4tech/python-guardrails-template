"""Fixture: an entity that is identified by its identifier."""

from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class Account:
    identifier: str
    balance: int

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Account) and self.identifier == other.identifier

    def __hash__(self) -> int:
        return hash(self.identifier)
