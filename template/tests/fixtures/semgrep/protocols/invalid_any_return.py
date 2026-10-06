"""Fixture of protocols whose methods hide their result behind Any."""

import typing
from typing import Any, Protocol, TypeVar

T = TypeVar("T", contravariant=True)


class ReportService(Protocol):
    def fetch_report(self, token_file: str) -> Any: ...


class RefreshService(Protocol):
    def refresh(self, token_file: str) -> typing.Any: ...


class ReportView(ReportService, Protocol):
    def show_report(self, report: str) -> Any: ...


class GenericReader(Protocol[T]):
    def read(self, source: T) -> Any: ...


class QualifiedReader(typing.Protocol):
    def read(self) -> Any: ...


class QuotedReader(Protocol):
    def read(self) -> "Any": ...


class OptionalReader(Protocol):
    def read(self) -> Any | None: ...


class ReversedOptionalReader(Protocol):
    def read(self) -> None | typing.Any: ...
