"""
Test prefix helper functions. Testing of the prefix and suffix options
is NOT done here, but in the main test module.
"""

from __future__ import unicode_literals
from itertools import islice

import pytest
from say import *


def test_numberer():
    say = Fmt(end='\n', prefix=numberer())
    assert say('this\nand\nthat') == '  1: this\n  2: and\n  3: that\n'

    say = Fmt(end='\n', prefix=numberer(template='{n:>4d}: ', start=100))

    assert say('this\nand\nthat') == ' 100: this\n 101: and\n 102: that\n'

def test_numberer_sequences():
    # first a one-shot
    nr = numberer(start=10)
    assert list(islice(nr, 0, 4)) == [' 10: ', ' 11: ', ' 12: ', ' 13: ']
    nr.reset()
    assert list(islice(nr, 0, 4)) == [' 14: ', ' 15: ', ' 16: ', ' 17: ']

    # and a multi-shot
    nr = numberer(start=10, oneshot=False)
    assert list(islice(nr, 0, 4)) == [' 10: ', ' 11: ', ' 12: ', ' 13: ']
    nr.reset()
    assert list(islice(nr, 0, 4)) == [' 10: ', ' 11: ', ' 12: ', ' 13: ']


def test_numberer_len():
    n = numberer()
    assert len(n) == 5
    n1 = next(n)
    assert len(n1) == 5
    assert len(n) == 5

    n2 = numberer(start=100)
    assert len(n2) == 5


def test_first_rest():
    fr = first_rest('>>> ', '... ')
    for i, v in enumerate(fr):
        if i == 0:
            assert v == '>>> '
        else:
            assert v == '... '
        if i > 4:
            break
    assert len(fr) == 4


def test_first_rest_reset():
    fr = first_rest(styled('\u25a0 ', 'blue'), '  ', oneshot=False)
    assert len(fr) == 2
    for i in range(4):
        if i:
            assert next(fr) == '  '
        else:
            assert next(fr) == '\x1b[34m\u25a0 \x1b[0m'
    fr.reset()
    # should be identical to above
    for i in range(4):
        if i:
            assert next(fr) == '  '
        else:
            assert next(fr) == '\x1b[34m\u25a0 \x1b[0m'
