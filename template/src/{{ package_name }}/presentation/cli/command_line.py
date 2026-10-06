"""The command line's arguments."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Write notes down and read them back.")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="write a note")
    add.add_argument("text")
    listing = commands.add_parser("list", help="show the notes")
    listing.add_argument("--last", type=int, help="show only the latest notes")
    return parser
