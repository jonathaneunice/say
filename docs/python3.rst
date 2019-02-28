Python 3
========

Say works virtually the same way in Python 2 and Python 3. This can simplify
software that should work across the versions, without the hassle
of ``from __future__ import print_function``.

``say`` attempts to mask some of the quirky complexities of the 2-to-3 divide,
such as string encodings and codec use. In general, things work best if
you use Unicode strings any time you need to use non-ASCII characters.
In Python 3, this is automatic.

If you are supporting Python 2, recommend you use this import::

    from __future__ import unicode_literals

To default strings to Unicode strings.

And if you are migrating to Python 3.6's new f-strings, there is a 
compatibility shim / polyfill that may be helpful:

    from say import f

    condition = 'good'
    print(f('this is {condition}'))

While not quite as elegant as the new f-string syntax ``f'this is {condition}'``, it has the virtue of working broadly all the way back to Python 2.6.
