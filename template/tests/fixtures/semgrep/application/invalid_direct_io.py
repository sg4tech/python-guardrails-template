"""Fixture containing direct I/O in an application module."""

import sqlite3
import subprocess
from pathlib import Path


def execute(path: Path) -> None:
    """Perform operations forbidden to application code."""
    sqlite3.connect("catalogue.db")
    path.read_text()
    path.write_text("catalogue")
    open("catalogue.txt")
    subprocess.run(["true"], check=True)
    subprocess.Popen(["true"])
