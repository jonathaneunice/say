"""Line prefixers. Or suffixers, if you read RTL."""

from ansiwrap import ansilen
from .util import _PY2

class numberer(object):

    """
    A class-based factory for numbering generators. Rather like Python 2's
    ``xrange`` (or Python 3's ``range``), but intended to number lines in a file
    so it uses natural numbers starting at 1, not the typical Python 'start at
    0'. Also, returns formatted strings, not integers. Improves on what's
    possible as a functional generator on numberer because it can compute and
    return its own length.
    """

    def __init__(self, start=1, template="{n:>3}: "):
        """
        Make a numberer.
        """
        self.n = start
        self.template = template
        self._formatted = None

    def __next__(self):
        """
        Return the next numbered template.
        """
        t = self.template
        if self._formatted:
            result = self._formatted
            self._formatted = None
        else:
            result = t.format(n=self.n)
        self.n += 1
        return result

    if _PY2:
        next = __next__

    def __len__(self):
        """
        What is the string length of the instantiated template now? NB This can change
        over time, as n does. Fixed-width format strings limit how often it can change
        (to when n crosses a power-of-10 boundary > the fixed template length
        can accommodate). This implementation saves the templated string it has created
        for reuse.
        """
        t = self.template
        result = t.format(n=self.n)
        self._formatted = result
        return ansilen(result)

    # TODO: Revisit this strategy for prefix length compuation. Probably
    #       making too complicated. Just generate the string and then
    #       compute its ANSI length. To be absolutely, completely correct,
    #       would probably require a peekable generator front-end and a
    #       wrapping post-processor that checks results and invokes a
    #       rework of line M... for any line M that is found to have
    #       changed its prefix length from the prior. Because wrapping is
    #       not prefix-length savvy.


def first_rest(first, rest):
    """
    Line prefixer (or suffixer) that gives one string for the first line, and
    an alternate string for every subsequent line. For implementing schemes
    like the Python REPL's '>>> ' followed by '... '.
    """
    yield first
    while True:
        yield rest

    # FIXME: A simple first_rest implementation is sweet, but will
    #        not play well with wrapping, because it cannot generate
    #        a proper len.
