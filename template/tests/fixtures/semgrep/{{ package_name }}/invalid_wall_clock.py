"""Fixture reading the wall clock outside the clock adapter."""

import datetime
import time
from datetime import date
from datetime import datetime as moment


def read_the_clock() -> None:
    datetime.datetime.now()
    datetime.datetime.utcnow()
    datetime.datetime.today()
    datetime.date.today()
    date.today()
    moment.now()
    time.time()
    time.time_ns()
