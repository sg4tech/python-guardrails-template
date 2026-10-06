"""Fixture: a test of the composition root may assert; only the package itself is restricted."""


def test_wiring() -> None:
    assert [value for value in (1, 2) if value]
