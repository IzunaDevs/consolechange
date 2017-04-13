from setuptools import setup
from setuptools.extension import Extension
import sys

requirements = []

version = '0.0.2'

if sys.platform != 'cygwin':
    _consolechange = Extension('consolechange._consolechange', ['consolechange/_consolechange.c'])
else:
    _consolechange = Extension('consolechange._consolechange',
                               library_dirs=['/usr/local/bin'],
                               sources=['consolechange/_consolechange.c'])


if not version:
    raise RuntimeError('version is not set')

try:
    with open('README.rst') as f:
        readme = f.read()
except FileNotFoundError:
    readme = ""

setup(name='consolechange',
      author='Decorater',
      author_email='seandhunt_7@yahoo.com',
      url='https://github.com/AraHaan/consolechange',
      bugtrack_url='https://github.com/AraHaan/consolechange/issues',
      version=version,
      packages=['consolechange'],
      ext_modules=[_consolechange],
      license='MIT',
      description='Package that allows changing the Console (Terminal) title in an platform independent way.',
      long_description=readme,
      maintainer_email='seandhunt_7@yahoo.com',
      download_url='https://github.com/AraHaan/consolechange',
      include_package_data=True,
      install_requires=requirements,
      platforms='Any',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)
