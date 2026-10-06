"""Fixture using only the pure parts of urllib."""
# ruff: noqa: F401, I001

from urllib.parse import parse_qs, urlencode as request, urlsplit
