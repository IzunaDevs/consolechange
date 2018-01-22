"""
Package that allows changing
the Console (Terminal) title in
an platform independent way.
"""

try:
    from ._consolechange import *
except ImportError:
    # pass the exception as the
    # c extension is not available
    # so this might mean that setup
    # needs the version from this script.
    pass


if _consolechange is not None:
  __all__ = _consolechange.all_members
  consoletitle = _consolechange.consoletitle
  consolesize = _consolechange.consolesize

__version__ = '0.0.3'
