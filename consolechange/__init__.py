"""
Package that allows changing
the Console (Terminal) title in
an platform independent way.
"""

try:
    from . import _consolechange
except ImportError:
    # the c extension is not available
    # so this might mean that setup
    # needs the version from this script.
    _consolechange = None


if _consolechange is not None:
    __all__ = _consolechange.all_members
    consoletitle = _consolechange.consoletitle

__version__ = '0.0.3'
