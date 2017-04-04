/*
 * Python extension module that automates the console
 * (or terminal) title change stuff for you that works for 
 * most (if not all) platforms in an single python
 * function (Unlike the multiple ways people
 * can do it already in python that requires using
 * sys.platform to get if it is windows or not just
 * to set it). This is useful as then it allows much
 * simpler and platform independent code without the need
 * to use sys.platform for any of it just to set an console
 * (Terminal in unix) title.
 */
#include <Python.h>
#include <stdio.h>
#ifdef _WIN32
#include <windows.h>
#endif

static PyObject *
consoletitle(PyObject *self, PyObject *args) {
  const char *title;
  if (!PyArg_ParseTuple(args, "s", &title))
      return NULL;
#if defined(_WIN32)
  SetConsoleTitleA(title);
#elif defined(__linux__) || defined(__CYGWIN__)
  printf("\033]2;%s\007\n\033[1A", title);
#else
  printf("\033]0;%s\007", title);
#endif
  Py_RETURN_NONE;
}

static PyMethodDef _consolechange_methods[] = {
  {"consoletitle", consoletitle, METH_VARARGS, "Sets the console title in a platform independent way."},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef _consolechangemodule = {
  PyModuleDef_HEAD_INIT, "_consolechange", "Python extension module that automates the console (or terminal) title change stuff for you that works for most (if not all) platforms in an single python function (Unlike the multiple ways people can do it already in python that requires using sys.platform to get if it is windows or not just to set it). This is useful as then it allows much simpler and platform independent code without the need to use sys.platform for any of it just to set an console (Terminal in unix) title.", -1, _consolechange_methods
};

PyMODINIT_FUNC
PyInit__consolechange(void)
{
  return PyModule_Create(&_consolechangemodule);
}
