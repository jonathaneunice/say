Prefixes and Suffixes
=====================

Every line can be given a prefix or suffix, if desired. For example::

    with say.settings(prefix='> '):
        say('this')
        say('that')

Will give what text email and Markdown consider a quoted block look::

    > this
    > that

Or if you'd like some text to be line-quoted with blue marks::

    say(text, prefix=styled('> ', 'blue'))

Or if you'd like output numbered::

    say.set(prefix=numberer())
    say('this\nand\nthat')

yields::

      1: this
      2: and
      3: that

You can instantiate different numberers for different files, and if you
like, use the ``start`` keyword argument to start a ``numberer`` on
a designated value.

Aother common prefixing scenario is needing to use one prefix on the
first line, but a second prefix on the remainder of lines. The Python
REPL uses this scheme, for example, with the prefix strings ``'>>> '``
and ``'... '``. If you'd like that scheme::

    say(text, prefix=first_rest('>>> ', '... '))

If you want a prefixer to start and run forever, the above is sufficient.
If you want a prefixer to reset itself every time it's invoked in a ``say()``,
initialize it with the kwarg ``oneshot=False``.

For example, to put a blue Unicode square as a hanging indicator of where a
paragraph starts::

    bluesquare = first_rest(styled('\u25a0 ', 'blue'), '  ', oneshot=False)
    say(text, prefix=bluesquare)

Beneath the Covers
------------------

Prefixers are essentially generator objects, but with several tweaks. They
support ``len()`` so that layout code can determine how much space to allot for
the prefix, and they can be easily reset to their starting point. If they're
designed multi-shot (e.g. ``oneshot=False``),  they'll be auto-reset on each
call of ``say()``.
