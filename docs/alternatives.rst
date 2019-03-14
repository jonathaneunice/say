Alternatives
============

* f-strings. As of Python 3.6, Python finally has formatted strings
  that are in-place interpolated. Thank you, `PEP 498
  <https://www.python.org/dev/peps/pep-0498/>`_. Some decades after Perl, PHP,
  Ruby, et al, but *bravo!* nonetheless. In many cases, if all you need are
  interplated strings, f-strings are grand. Just one of many reasons to upgrade
  to the latest modern Python builds. Sadly, f-strings lack the easy coloring,
  wrapping, and other formatting functions ``say`` builds in. But f-strings are
  quite compatible with ``say``, so feel free to use them together.

* `ScopeFormatter <http://pypi.python.org/pypi/ScopeFormatter>`_
  provides variable interpolation into strings. It is amazingly
  compact and elegant. Sadly, it only interpolates Python names, not full
  expressions. ``say`` has full expressions, as well as a framework for
  higher-level printing features beyond ``ScopeFormatter``'s...um...scope.

* `interpolate <https://pypi.python.org/pypi/interpolate>`_ is
  similar to ``say.fmt()``, in that it can
  interpolate complex Python expressions, not just names.
  Its ``i % "format string"`` syntax is a little odd, however, in
  the way that it re-purposes Python's earlier ``"C format string" % (values)``
  style ``%`` operator. It also depends on the native ``print`` statement
  or function, which doesn't help bridge Python 2 and 3.

* Even simpler are invocations of ``%`` or ``format()``
  using ``locals()``. E.g.::

       name = "Joe"
       print "Hello, %(name)!" % locals()
       # or
       print "Hello, {name}!".format(**locals())

  Unfortunately this has even more limitations than ``ScopeFormatter``: it
  only supports local variables, not globals or expressions. And the
  interpolation code seems gratuitous. Simpler::

      say("Hello, {name}!")