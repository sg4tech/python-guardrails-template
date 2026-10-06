"""Fixture standing in for the one module that may read the wall clock."""

from datetime import UTC, datetime


def utc_now() -> datetime:
    return datetime.now(UTC)
