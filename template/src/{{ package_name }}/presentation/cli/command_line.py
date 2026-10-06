"""The command line's arguments."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Write notes down and read them back.")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="write a note")
    add.add_argument("text")
    commands.add_parser("list", help="show every note")
    return parser
