"""Fixture containing filesystem probes in an application module."""

from pathlib import Path


def probe(path: Path, other: Path) -> bool:
    path.is_file()
    path.is_dir()
    path.exists()
    path.resolve()
    path.stat()
    return path.samefile(other)
