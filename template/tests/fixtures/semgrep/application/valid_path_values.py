"""Fixture using paths only as values."""

from pathlib import Path


def describe(path: Path) -> Path:
    return (path.parent / path.name).with_suffix(".txt")
