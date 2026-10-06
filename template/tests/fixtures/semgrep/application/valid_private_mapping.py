"""Fixture with a private implementation detail that is not a public contract."""

from collections.abc import Mapping


def _read_identifier(payload: Mapping[str, object]) -> str:
    """Read a value from an internal implementation detail."""
    return str(payload["identifier"])
