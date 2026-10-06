"""Fixture building objects by copying another object's fields one by one."""

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Stored:
    identifier: str
    title: str
    status: str


@dataclass(frozen=True)
class Shown:
    identifier: str
    title: str
    status: str
    views: int = 0


def show(stored: Stored) -> Shown:
    return Shown(identifier=stored.identifier, title=stored.title, status=stored.status)


def show_in_another_order(stored: Stored, views: int) -> Shown:
    return Shown(
        status=stored.status, views=views, identifier=stored.identifier, title=stored.title
    )


def copy_onto(shown: Shown, stored: Stored) -> Shown:
    return replace(shown, identifier=stored.identifier, title=stored.title, status=stored.status)
