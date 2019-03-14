Notes
=====

* The ``say`` name was inspired by Perl's `say <http://perldoc.perl.org/functions/say.html>`_,
  but the similarity stops there.

* Automated multi-version testing managed with the wonderful
  `pytest <http://pypi.org/project/pytest>`_,
  `pytest-cov <http://pypi.org/project/pytest-cov>`_,
  `coverage <http://pypi.org/project/coverage>`_,
  and `tox <http://pypi.org/project/tox>`_.
  Packaging linting with `pyroma <https://pypi.org/project/pyroma>`_.

* Successfully packaged for, and tested against, all late-model versions of
  Python: 2.7, 3.5, 3.6, and 3.7 as well as late models of PyPy and PyPy3. It
  may work on Python 2.6 and earlier builds of 3.x (it did historically), but
  testing can no longer verify that. Also, those are such old Python builds!
  Upgrade to 3.7 or later ASAP!

* ``say`` has greater ambitions than just simple template prßinting. It's
  part of a larger rethinking of how output should be formatted.
  ``say.Text``, `show <http://pypi.org/project/show>`_, and `quoter
  <http://pypi.org/project/quoter>`_ are other down-payments on this
  larger vision. Stay tuned.

* In addition to being a practical module in its own right, ``say`` is
  testbed for `options <http://pypi.org/project/options>`_, a package
  that provides high-flexibility option, configuration, and parameter
  management.

* The author, `Jonathan Eunice <mailto:jonathan.eunice@gmail.com>`_ or
  `@jeunice on Twitter <http://twitter.com/jeunice>`_
  welcomes your comments and suggestions. If you're using ``say`` in your own
  work, drop me a note and tell me how you're using it, how you like it,
  and what you'd like to see!


To-Dos
======

* Further formatting techniques for easily generating HTML output and
  formatting non-scalar values.
* Complete the transition to per-method styling and more refined named
  styles.
* Provide code that allows ``pylint`` to see that variables used inside
  the ``say`` and ``fmt`` format strings are indeed thereby used.
