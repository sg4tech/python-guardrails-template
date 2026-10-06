"""Fixture of a fat command handler, used to pin which modules the handler rules cover."""

import time
from typing import Any


def handle_link(args: Any, service: Any, view: Any, dry_run: bool) -> int:
    del service, view
    print(args, dry_run)
    return 0


def load(path: Any) -> Any:
    time.sleep(0.1)
    return open(path)
