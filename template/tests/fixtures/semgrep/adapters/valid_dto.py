"""Fixture with a Pydantic DTO confined to an adapter."""

from pydantic import BaseModel


class ExternalPayload(BaseModel):
    """Validate an external payload at the adapter boundary."""

    identifier: str
