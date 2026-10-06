"""Fixture reading the environment outside composition and adapter configuration."""

import os
from os import environ, getenv


def read_the_environment() -> None:
    os.environ["A"]
    os.environ.get("B")
    os.getenv("C")
    environ.get("D")
    getenv("E")
