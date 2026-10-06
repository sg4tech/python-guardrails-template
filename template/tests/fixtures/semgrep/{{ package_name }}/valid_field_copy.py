"""Fixture building objects without copying another object's fields one by one."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Stored:
    identifier: str
    title: str
    status: str


@dataclass(frozen=True)
class Shown:
    stored: Stored
    views: int = 0


@dataclass(frozen=True)
class Labelled:
    identifier: str
    title: str
    status: str


def show(stored: Stored, views: int) -> Shown:
    return Shown(stored, views)


def label_two(stored: Stored) -> Labelled:
    return Labelled(identifier=stored.identifier, title=stored.title, status="new")


def label_renamed(stored: Stored) -> Labelled:
    return Labelled(identifier=stored.identifier, title=stored.status, status=stored.title)


def label_from_several(first: Stored, second: Stored) -> Labelled:
    return Labelled(identifier=first.identifier, title=second.title, status=first.status)


def log_fields(stored: Stored, log: "Logger") -> None:
    log.info(identifier=stored.identifier, title=stored.title, status=stored.status)


class Logger:
    def info(self, **fields: str) -> None:
        del fields
