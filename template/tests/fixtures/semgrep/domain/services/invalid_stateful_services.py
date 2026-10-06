"""Fixture: services that keep state between calls."""

counter = 0


def bump() -> None:
    global counter
    counter += 1


class Cache:
    def __init__(self) -> None:
        self.items: dict[str, int] = {}

    def remember(self, key: str) -> None:
        self.items[key] = 1
        self.last = key
