"""Fixture with raw external payload contracts in the application layer."""

import collections.abc
import typing
from collections.abc import Mapping

from pydantic import BaseModel


class ExternalPayload(BaseModel):
    """Pydantic must not be part of an application-layer contract."""

    identifier: str


def accept_mapping(payload: Mapping[str, object]) -> None:
    """Accept a raw payload."""
    del payload


def return_mapping() -> Mapping[str, object]:
    """Return a raw payload."""
    return {"identifier": "video-1"}


def accept_dict(payload: dict[str, object]) -> None:
    """Accept a raw payload."""
    del payload


def return_dict() -> dict[str, object]:
    """Return a raw payload."""
    return {"identifier": "video-1"}


def accept_qualified_mapping(payload: collections.abc.Mapping[str, object]) -> None:
    """Accept a raw payload through its qualified name."""
    del payload


def return_typing_mapping() -> typing.Mapping[str, object]:
    """Return a raw payload through its qualified name."""
    return {"identifier": "video-1"}
