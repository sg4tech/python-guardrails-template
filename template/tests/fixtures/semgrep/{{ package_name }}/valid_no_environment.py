"""Fixture that receives its settings instead of reading them."""

from collections.abc import Mapping


def chosen(settings: Mapping[str, str]) -> str:
    return settings.get("A", "")
