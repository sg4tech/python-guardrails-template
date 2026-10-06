"""Fixture containing direct I/O inside PEP 695 generic definitions in an application module."""

from pathlib import Path


class Loader[ValueT]:
    """Generic class whose body must still be analysed."""

    def load(self, path: Path) -> str:
        with open(path) as handle:
            return handle.read()


def first[ItemT: object](items: list[ItemT]) -> ItemT:
    """Generic function with a bound whose body must still be analysed."""
    open("catalogue.txt")
    return items[0]
