"""A note: a short text written at a known moment."""

from dataclasses import dataclass
from datetime import datetime


class EmptyNoteError(ValueError):
    """A note must say something."""


@dataclass(frozen=True)
class Note:
    text: str
    written_at: datetime

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise EmptyNoteError("a note must not be empty")
