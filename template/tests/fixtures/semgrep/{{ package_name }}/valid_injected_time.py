"""Fixture that gets its time from outside and only measures durations itself."""

import time
from collections.abc import Callable
from datetime import datetime


def stamp(clock: Callable[[], datetime]) -> datetime:
    return clock()


def deadline(timeout_seconds: float) -> float:
    return time.monotonic() + timeout_seconds
