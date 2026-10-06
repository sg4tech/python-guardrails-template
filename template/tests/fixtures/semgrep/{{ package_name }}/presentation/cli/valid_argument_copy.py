"""Fixture turning parsed command-line arguments into a typed value, which is a boundary."""

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Overlay:
    video: Path
    music: Path
    output: Path


def overlay(parsed: argparse.Namespace) -> Overlay:
    return Overlay(video=parsed.video, music=parsed.music, output=parsed.output)
