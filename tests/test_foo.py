from __future__ import annotations

from letspython.foo import foo


def test_foo() -> None:
    assert foo("foo") == "foo"
