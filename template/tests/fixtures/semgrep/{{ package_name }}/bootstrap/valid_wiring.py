"""Fixture: construction and wiring the composition-root rule accepts."""

import os
from functools import partial
from pathlib import Path
from typing import Any


def create_reader(database: Path) -> Any:
    return {"path": database}


def create_service(clock: Any) -> Any:
    database = Path(os.environ.get("DATABASE", "catalogue.sqlite3"))
    reader = create_reader(database)
    return partial(dict, reader=reader, clock=clock, later=lambda: create_reader(database))
