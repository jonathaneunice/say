Where and Wen You Like
======================

``say`` is organized to put output to the place or places you want, and
to do so only when you want. The destinations and on/off status
can easily be changed.

Where
-----

``say()`` writes to a list of files. By default the list is just
standard output (``sys.stdout``). But with a simple configuration
call, it will write to different--even multiple--files::

    say.set(files=[sys.stdout, "report.txt"])
    say(...)   # now prints to both sys.stdout and report.txt

Note that you never even had to open ``"report.txt"``. It's okay
if you pass in open file objects, but if you pass in strings, they'll
be interpreted as file names of intended output files, and opened for
you (with UTF-8 encoding, even).

With the above lines, you're now both writing program output as normal
*and* capturing it to a file for later inspection and use. Try that
with your normal ``print`` statement/function! It can be done...if you
double the number of print calls.

Note however that if you pass a file descriptor that you open yourself,
and you're using Python 2, *you* are responsible for opening the file
in a way that supports a proper encoding--a detail that Python 3 handles
for you. Please see the Encodings and Unicode section for more details and
examples.

``say`` does, by the by, also support the ``file`` argument in the same way
Python 3's ``print()`` does. This is a less typical use, but is provided for
compatiblity for those converting from ``print()`` calls.

You can also define
your own targeted ``Say`` instances, for example for error reporting::

    err = say.clone(files=[sys.stderr, 'error.txt'])
    err("Failed with error {errcode}")  # writes in both places
    say("something else")   # independent of err

When
----

Output is great, but sometimes you need to go silent.
If you want to stop printing for a while::

    say.set(silent=True)  # no printing until set to False

Or transiently::

    say(...stuff..., silent=not verbose) # prints iff bool(verbose) is True

Of course, you don't have to print at all.
``fmt()`` works exactly like ``say()`` and inherits most of its options,
but doesn't print. (The ``C`` analogy: ``say`` **:** ``fmt`` **::** ``printf``
**:** ``sprintf``.)

How
---

On occasion it can be valuable to use ``say`` but not its varaible
interpolation. The ``say.verbatim()`` method does this. All the
standard formmating applies, but ``{}`` variable templates will not
be filled in.
