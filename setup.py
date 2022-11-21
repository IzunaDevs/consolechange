from setuptools import setup
from setuptools.extension import Extension
import sys


def get_extensions():
    """
    lists the extensions to build with a compiler.
    """
    if sys.platform != 'cygwin':
        _consolechange = Extension(
            'consolechange._consolechange',
            sources=['consolechange/_consolechange.c'])
    else:
        _consolechange = Extension(
            'consolechange._consolechange',
            library_dirs=['/usr/local/bin'],
            sources=['consolechange/_consolechange.c'])
    return [_consolechange]


setup_args = dict(
    ext_modules=get_extensions())

setup(**setup_args)
