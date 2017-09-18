from setuptools import setup
from setuptools.extension import Extension
import sys

requirements = []

version = '0.0.2'

if sys.platform != 'cygwin':
    _consolechange = Extension('consolechange._consolechange', sources=[
        'consolechange/_consolechange.c'])
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
      author='IzunaDevs',
      author_email='izunadevs@martmists.com',
      url='https://github.com/IzunaDevs/consolechange',
      bugtrack_url='https://github.com/IzunaDevs/consolechange/issues',
      version=version,
      packages=['consolechange'],
      data_files=[('consolechange', ['consolechange/_consolechange.c.h'])],
      ext_modules=[_consolechange],
      license='MIT',
      description='Package that allows changing the Console (Terminal) title in an platform independent way.',
      long_description=readme,
      maintainer_email='izunadevs@martmists.com',
      download_url='https://github.com/IzunaDevs/consolechange',
      include_package_data=True,
      install_requires=requirements,
      platforms='Any',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: C',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ]
)
