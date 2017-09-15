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


def _write_c_files():
    c_file_1 = """#include <Python.h>
#include <stdio.h>
#ifdef _WIN32
#include <windows.h>
#endif
#include \"_consolechange.c.h\"

static PyObject *
consoletitle(PyObject *self, PyObject *args) {
  const char *title;
  if (!PyArg_ParseTuple(args, \"s\", &title))
      return NULL;
  _change_title(title);
  Py_RETURN_NONE;
}

static PyObject *
consolesize(PyObject *self, PyObject *args) {
  return _change_size(args);
}

static PyMethodDef _consolechange_methods[] = {
  {\"consoletitle\", consoletitle, METH_VARARGS,
   CONSOLETITLE__DOC__},
  {\"consolesize\", consolesize, METH_VARARGS,
   CONSOLESIZE__DOC__},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef _consolechangemodule = {
  PyModuleDef_HEAD_INIT, \"_consolechange\",
  _CONSOLECHANGE__DOC__, -1, _consolechange_methods
};

PyMODINIT_FUNC
PyInit__consolechange(void)
{
  return PyModule_Create(&_consolechangemodule);
}
"""
    c_file_2 = """/*
 * _consolechange.c.h
 */
#define _CONSOLECHANGE__DOC__ \\
"Python extension module that automates" \\
" the console (or terminal) title change" \\
" stuff for you that works for most (if " \\
"not all) platforms in an single python " \\
"function (Unlike the multiple ways " \\
"people can do it already in python that" \\
" requires using sys.platform to get if " \\
"it is windows or not just to set it). " \\
"This is useful as then it allows much " \\
"simpler and platform independent code " \\
"without the need to use sys.platform " \\
"for any of it just to set an console " \\
"(Terminal in unix) title."
#define CONSOLETITLE__DOC__ \\
"Sets the console (terminal) title in " \\
"a platform independent way."
#define CONSOLESIZE__DOC__ \\
"Sets the console size. On Windows " \\
"this resizes the console, on any " \\
"other platforms it just returns None."

void _change_title(const char *title) {
#if defined(_WIN32)
  SetConsoleTitleA(title);
#elif defined(__linux__) || defined(__CYGWIN__)
  printf("\\033]2;%s\\007\\n\\033[1A", title);
#else
  printf("\\033]0;%s\\007", title);
#endif
}

static PyObject *
_change_size(PyObject *args) {
#if defined(_WIN32)
  int rows, cols;
  if (!PyArg_ParseTuple(args, "ii", &rows, &cols))
      return NULL;
  char buffer [256];
  snprintf(buffer, sizeof(buffer),
    "mode con: cols=%i lines=%i", rows, cols);
  system(buffer);
#endif
  Py_RETURN_NONE;
}
"""
    with open('consolechange/_consolechange.c', 'w') as of:
        of.write(c_file_1)
    with open('consolechange/_consolechange.c.h', 'w') as of:
        of.write(c_file_2)

_write_c_files()

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
      data_files=[('consolechange', ['consolechange/_consolechange.c.h'])],
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
