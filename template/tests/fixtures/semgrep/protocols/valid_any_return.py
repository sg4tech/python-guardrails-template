"""Fixture of protocols that return concrete boundary types, next to Any the rule allows."""

from typing import Any, Protocol, TypeVar

T = TypeVar("T", covariant=True)


class ReportService(Protocol):
    def fetch_report(self, token_file: str) -> tuple[str, ...]: ...


class ReportView(Protocol):
    def show_report(self, report: Any) -> None: ...


class ConsoleView:
    def render(self) -> Any:
        return None


class GenericReader(Protocol[T]):
    def read(self) -> T | None: ...

    def to_mapping(self) -> dict[str, Any]: ...

    def kind(self) -> "AnyKind": ...

    def fallback(self) -> "None | AnyKind": ...


class AnyKind:
    pass
