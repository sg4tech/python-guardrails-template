"""Fixture importing the I/O parts of urllib in an application module."""
# ruff: noqa: F401, I001

import urllib.error
import urllib.request
from urllib import error, request
from urllib.error import URLError
from urllib.request import urlopen
from urllib import (
    parse,
    request as fetch,
)
import urllib.parse
