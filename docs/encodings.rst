Encodings and Unicode
=====================

Character encodings remain a fractious and often exasperating part of IT.

If you are deal with more than ASCII characters with any regularity
whatsoever, for the love of God and all that is holy, use Python 3.
It has *greatly* superior support for Unicode characters, and will
generally make your life much eaiser.

``say()`` and ``fmt()`` try to avoid encoding gotchas by working with
Unicode strings.

In Python 3, all strings are Unicode strings, and all files are inherently smart
enough to read and write to reasonable encodings needed to store Unicode strings
on disk. But in Python 2, there is a choice between ``str`` and ``unicode``, and
most files are *not* smart enough to use rational encodings. Indeed, files that
appear to have an ``encoding`` attribute will not let you set that attribute,
and they will not enforce that encoding when doing file IO. *!@#$%^&!!!*

So if you must use Python 2:

* Use ``unicode`` strings whenever possible.

* If you use the basie ``str`` type, include *only* ASCII characters, not
  encoded bytes from UTF-8 or whatever. If you don't do this, any trouble results
  be on your head.

* If ``say`` opens a file for you, it will do it with the ``codecs`` module
  with a default encoding of UTF-8. If you have ``say``
  write to a file that you open, you **must**  use
  ``codecs.open()``, ``io.open()``, or a similar mechanism that supports
  proper encoding. Else errors will result.

``say`` has a long history of trying to make Python 2 automatically "do the
right thing" even when basic Python 2 facilities do not. We have discovered,
like so many others before us, that was a fool's errand. Python 2 is simply
ill-prepared for day-in, day-out use of Unicode characters that are all around
us in the modern global world. While ``say`` continues some of this with respect
to the default standard output (``stdout``) stream, many of the previous
back-bends to support auto-encoding have been withdrawn. If you choose to use
Python 2, *you* are responsible for opening files in a responsible,
encoding-friendly way.::

    from codecs import open

    with open('outfile.txt', 'w', encoding='utf-8') as f:
        say(u'Contains\u2012Unicode!', file=f)
