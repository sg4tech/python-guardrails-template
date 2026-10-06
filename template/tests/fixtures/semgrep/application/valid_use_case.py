"""Fixture containing application orchestration through a port."""

from typing import Protocol


class CatalogueReader(Protocol):
    """Provide catalogue data at the application boundary."""

    def list_titles(self) -> tuple[str, ...]: ...


def list_titles(reader: CatalogueReader) -> tuple[str, ...]:
    """Delegate data access to the supplied port."""
    return reader.list_titles()
