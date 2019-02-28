Colors and Styles
=================

``say`` has built-in support for style-driven formatting. By default,
ANSI terminal colors and styles are automagically supported.

::

    answer = 42

    say("The answer is {answer:style=bold+red}")

This uses the `ansicolors <https://pypi.python.org/pypi/ansicolors>`_
module, though with a slightly more permissive syntax. Available colors are
'black', 'blue', 'cyan', 'green', 'magenta', 'red', 'white', and 'yellow'.
Available styles are 'bold', 'italic', 'underline', 'blink', 'blink2',
'faint', 'negative', 'concealed', and 'crossed'. These styles can be
combined with a ``+`` or ``|`` character. Note, however, that not all styles
are available on every terminal.

.. note:: When naming a style within the template braces (``{}``) of format strings, you can quote the style name or not. ``fmt("{x:style=red+bold}")`` is equivalent to ``fmt("{x:style='red+bold'}")``.

You can define your own styles::

    say.style(warning=lambda x: color(x, fg='red'))

Because styles are defined through executables (lambdas, usually), they can
include decisions or text transformations of arbitrary complexity.
For example::


    say.style(redwarn=lambda n: color(n, fg='red', style='bold') if int(n) < 0 else n)
    ...
    say("Result: {n:style=redwarn}")

That will display the number ``n`` in bold red characters, but only if it's value is
negative. For positive numbers, ``n`` is displayed normally.

Or define a style where a message is surrounded by red stars::

    say.style(stars=lambda x: fmt('*** ', style='red') + \
                              fmt(x,      style='black') + \
                              fmt(' ***', style='red'))
    say.style(redacted=lambda x: 'x' * len(x))

    message = 'hey'
    say(message, style='stars')
    say(message, style='redacted')

Yields::

    *** hey ***
    xxx

(with red stars)

.. note:: Style defining lambdas (or functions) take string arguments. If the string is logically a number, it must be then cast into an ``int``, ``float``, or whatever. The code must ultimate return a string.

You can also apply a style to the entire contents of a ``say`` or ``fmt`` invocation::

    say("There is green everywhere!", style='green|underline')

(Whether or not you get underlines, and what shade of green, those depend on the terminal
you use.)

Or try::

    say('a long paragraph with gobs of text',
        style='indigo', prefix=numberer(), wrap=25)

Which yields::

    1: a long paragraph
    2: with gobs of text

The lines are numbered, they're wrapped to 25 characters, and (on most
consoles), the text appears in the color indigo. If you don't think that's an
impressive amount of formatting for one function call, you've never tried to
implement similar formatting without ``say``'s help.

If you want to get really fancy, give the line numbers their own independent
styling::

    linenum = numberer(template=color('{:>3}', fg='hotpink'))
    say('a long paragraph with gobs of text',
        style='indigo', prefix=linenum, wrap=25)

This is just not something that's practical without ``say``, but easy with it.

Styled formatting is an extremely powerful approach, giving the
same kind of flexibility and abstraction seen for styles in word processors and
CSS-based Web design. It will be further developed.
