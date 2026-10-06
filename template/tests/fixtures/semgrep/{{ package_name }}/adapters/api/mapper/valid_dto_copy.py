"""Fixture mapping a platform's DTO into a domain value, which is a boundary."""

from dataclasses import dataclass


@dataclass(frozen=True)
class VideoDto:
    identifier: str
    title: str
    views: int


@dataclass(frozen=True)
class Video:
    identifier: str
    title: str
    views: int


def video_from_dto(video: VideoDto) -> Video:
    return Video(identifier=video.identifier, title=video.title, views=video.views)
