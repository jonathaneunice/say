"""
Test prefix helper functions. Testing of the prefix and suffix options
is NOT done here, but in the main test module.
"""

from say import *
import pytest


def test_numberer():
    say = Fmt(end='\n', prefix=numberer())
    assert say('this\nand\nthat') == '  1: this\n  2: and\n  3: that\n'

    say = Fmt(end='\n', prefix=numberer(template='{n:>4d}: ', start=100))

    assert say('this\nand\nthat') == ' 100: this\n 101: and\n 102: that\n'


def test_first_rest():
    for i, v in enumerate(first_rest('>>> ', '... ')):
        if i == 0:
            assert v == '>>> '
        else:
            assert v == '... '
        if i > 4:
            break


def test_len():
    n = numberer()
    assert len(n) == 5
    n1 = next(n)
    assert len(n1) == 5
    assert len(n) == 5
