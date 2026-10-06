"""Fixture standing in for a module that may read the environment."""

import os


def setting() -> str:
    return os.environ.get("A", "")
