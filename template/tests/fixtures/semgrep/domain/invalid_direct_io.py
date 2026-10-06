"""Fixture containing direct filesystem I/O in a domain module."""


def validate() -> None:
    open("catalogue.txt")
