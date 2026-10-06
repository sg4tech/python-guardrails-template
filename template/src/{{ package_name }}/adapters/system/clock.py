"""The only place that reads the wall clock; everything else receives the time."""

from datetime import UTC, datetime


class SystemClock:
    def now(self) -> datetime:
        return datetime.now(UTC)
