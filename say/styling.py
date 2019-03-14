"""
Module to handle styled printing
"""

from colors import color as _color, parse_rgb, COLORS, STYLES
from options.chainstuf import chainstuf
import sys
from .util import *


QUOTE_DELIM = ('"', "'")
QUOTE_DELIM_STR = ''.join(QUOTE_DELIM)

# TODO: implement a persistent Style object that say.style will return


def parse_color(c):
    """
    Shim between ansicolors.parse_rgb and previous expectations. Handles valid
    HTML color names and hex specs (e.g. #ffc823) properly, but not rgb(x,y,z)
    specs--not because of this code, but because of how style arguments are
    parsed upstream.
    """
    if c in COLORS:
        return c
    try:
        rgb = parse_rgb(c)
        if rgb:
            return rgb
    except ValueError:
        pass
    return None

    # FIXME: correctly pass in / parse rgb(x,y,x) color specs


class Relative(int):

    def __repr__(self):
        plus = '+' if self > 0 else ''
        return "{0}({1}{2})".format(self.__class__.__name__, plus, self)

    def __add__(self, other):
        value = int.__add__(self, other)
        return Relative(value) if isinstance(other, Relative) else value

    def __sub__(self, other):
        value = int.__sub__(self, other)
        return Relative(value) if isinstance(other, Relative) else value

    # TODO: figure out mul and div operations across Python 2 and 3 - useful to add?


class optdict(dict):
    """
    dict subclass that only initializes keys corresponding to non-empty value.
    Convenient for kwarg dicts that don't have to define default values.
    """
    def __init__(self, **kwargs):
        dict.__init__(self)
        for k,v in kwargs.items():
            if v:
                self[k] = v


class StyleDef(object):
    """
    Class defining a formatting style.
    """

    def __init__(self, *args, **kwargs):
        """
        Create a new StyleDef, remembering its settings.
        """
        self.name = kwargs.get('name', None)
        self.join = kwargs.get('join', None)
        if 'name' in kwargs:
            del kwargs['name']
        if 'join' in kwargs:
            del kwargs['join']
        self.sdef = styledef(*args, **kwargs)

    def __call__(self, item):
        """
        Apply this style to the given item.
        """
        result = self.join(item) if self.join else item
        result = _color(result, **self.sdef) if self.sdef else result
        return result


def styledef(*args, **kwargs):
    """
    Parses a style definition as given in args and kwargs.
    Return a dict that defines a given style definition. If it's an ANSI style
    being defined, whatever color is named first (if any) is assumed to be the
    foreground, the second the background. ANSI display styles (like 'bold') can
    be named anywhere.
    """
    kw = chainstuf()
    for arg in args:
        arg = arg.replace('+', '|').replace(',', '|').lower()
        parts = [p.strip() for p in arg.split('|')]
        fg, bg, styles = None, None, []
        for p in parts:
            pc = parse_color(p)
            # FIXME: note pc never used - parsing here just a validity check
            if pc is not None:
                if not fg:
                    fg = p
                elif not bg:
                    bg = p
                else:
                    raise ValueError('only fg and bg colors!')
            elif p in STYLES:
                styles.append(p)
            else:                           # pragma: no cover
                raise ValueError("Well! That's odd! {!r}".format(p))
        kw.update(optdict(fg=fg, bg=bg, style='|'.join(styles) if styles else None))
    kw.update(kwargs)
    return kw


def autostyle(*args, **kwargs):
    """
    Return a lambda that will later format a string with the given styledef.
    """
    sdef = styledef(*args, **kwargs)
    return lambda x: color(x, **sdef)


def color(item, **kwargs):
    """
    Like colors.color, except auto-casts to Unicode string if need be.
    """
    item_u = unicode(item) if not isinstance(item, basestring) else item
    return _color(item_u, **kwargs)


def styled(item, *args, **kwargs):
    """
    Like color, but can also include style names.
    Kind of an immediate-mode version of autostyle.
    """
    sdef = styledef(*args, **kwargs)
    return color(item, **sdef)
