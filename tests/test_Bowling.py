import pytest

from .context import bowling

def test_itIsWired():
    assert bowling.Bowling().isAlive()
