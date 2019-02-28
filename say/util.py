"""
Home for separable utility functions used in say
"""

import itertools
import sys
import types
import codecs

# Basic Python version compatibility
_PY2 = sys.version_info[0] == 2
if _PY2:
    from StringIO import StringIO
    basestring = basestring   # so that can be exported
    unicode = unicode         # so that can be exported
    stringify = lambda v: v if isinstance(v, basestring) else unicode(v)
else:
    from codecs import getencoder
    basestring = unicode = str
    from io import StringIO
    stringify = str


def is_string(v):
    """
    Is the value v a string? Useful especially in making a test that works on
    both Python 2.x and Python 3.x
    """
    return isinstance(v, basestring)


def opened(f):
    """
    If f is a string, consider it a file path; return an open file that is ready
    to write to that path. Otherwise, assume it is an already open file and just
    return it. If it is a list or tuple (possibly of mixed strings / file paths
    and open files, do this action all each member of the list.

    Uses codecs.open to add auto-encoding in Python 2
    """
    if isinstance(f, (tuple, list)):
        return [ opened(ff) for ff in f ]
    if is_string(f):
        return codecs.open(f, mode='w', encoding='utf-8')
    return f


def encoded(u, encoding):
    """
    Encode string u (denoting it is expected to be in Unicode) if there's
    encoding to be done. Tries to mask the difference between Python 2 and 3,
    which have different models of string processing, and different codec APIs
    and quirks. Some Python 3 encoders further require ``bytes`` in, not
    ``str``. These are first encoded into utf-8, encoded, then decoded.
    """
    if not encoding:
        return u
    elif _PY2:
        # Python 2 may not have the best handling of Unicode, but by
        # by God its encode operations are straightforward!
        return u.encode(encoding)
    else: # PY3
        encoder = getencoder(encoding)
        try:
            return encoder(u)[0]
        except TypeError: # needs bytes, not str
            try:
                ub = u.encode('utf-8') # to bytes
                ube = encoder(ub)[0]
                # return strings
                if isinstance(ube, bytes):
                    return ube.decode('utf-8')
                else:
                    return ube
            except Exception as e:
                raise e


        # NB PY3 requires lower-level interface for many codecs. s.encode('utf-8')
        # works fine, but others do not. Some codecs convert bytes to bytes,
        # and are not properly looked up by nickname (e.g. 'base64'). These are
        # managed by first encoding into utf-8, then if it makes sense decoding
        # back into a string. The others are things like bz2 and zlib--binary
        # encodings that have little use to us here.

        # There are also be some slight variations in results that will make
        # testing more fun. Possibly related to adding or not adding a terminal
        # newline.


def flatten(*args):
    """
    Like itertools.chain(), but will pretend that single scalar values are
    singleton lists. Convenient for iterating over values whether they're lists
    or singletons.
    """
    flattened = [x if isinstance(x, (list, tuple)) else [x] for x in args]
    return itertools.chain(*flattened)

    # would use ``hasattr(x, '__iter__')`` rather than ``isinstance(x, (list, tuple))``,
    # but other objects like file have ``__iter__``, which screws things up


def next_str(g):
    """
    Given a generator g, return its next result as a unicode string. If not a
    generator, just return the value as a unicode string.
    """
    try:
        value = next(g)
    except TypeError:
        value = g if g is not None else ''
    return unicode(value)


def get_stdout():
    """
    Say objects previously had their own output encoding mechanism. It is now
    simplified, pushing encoding responsibility onto whatever underlying file
    object (or file analog) is being written to. While generally a good
    decision, it causes problems on some terminals (e.g. Komodo IDE) that for
    some reason initialize sys.stdout's encoding to US-ASCII. In those cases,
    instead of returning sys.stdout per se, return a writer object that does a
    rational encoding (UTF-8).
    """
    if sys.stdout.encoding == 'UTF-8': # pragma: no cover
        return sys.stdout              # true almost universally - but not under test
    else:
        return codecs.getwriter('UTF-8')(sys.stdout)
