"""Fixture of thin command handlers next to composition code the handler rules do not cover."""

from datetime import datetime
from pathlib import Path
from typing import Any


def handle_report(args: Any, service: Any, view: Any) -> int:
    """Delegate one call, for the command, and render its result."""
    view.show_report(service.fetch_report(args.notes_file))
    return 0


def handle_sync(args: Any, service: Any, view: Any) -> int:
    service.synchronize(args.notes_file, args.database, view)
    return 0


def handle_login(args: Any, service: Any, view: Any) -> int:
    service.login(args.notes_file, args.settings_file, view)
    view.token_saved(args.notes_file)
    return 0


def main(command: str, command_line: Any) -> int:
    service = command_line.report
    if command == "report":
        return handle_report(Path("notes.json"), service, service)
    for item in [datetime.now(), Path.home()]:
        handle_sync(item, service, service)
    return 1 if command else 0


def _handle_private(arguments: Any) -> Any:
    return arguments
