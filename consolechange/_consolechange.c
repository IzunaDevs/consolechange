#include <Python.h>
#include <stdio.h>
#ifdef _WIN32
#include <windows.h>
#endif
#include "_consolechange.c.h"

static PyObject *
consoletitle(PyObject *self, PyObject *args) {
  const char *title;
  if (!PyArg_ParseTuple(args, "s", &title))
      return NULL;
  _change_title(title);
  Py_RETURN_NONE;
}

static PyObject *
consolesize(PyObject *self, PyObject *args) {
  return _change_size(args);
}

static PyMethodDef _consolechange_methods[] = {
  {"consoletitle", consoletitle, METH_VARARGS,
   CONSOLETITLE__DOC__},
  {"consolesize", consolesize, METH_VARARGS,
   CONSOLESIZE__DOC__},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef _consolechangemodule = {
  PyModuleDef_HEAD_INIT, "_consolechange",
  _CONSOLECHANGE__DOC__, -1, _consolechange_methods
};

PyMODINIT_FUNC
PyInit__consolechange(void)
{
  return PyModule_Create(&_consolechangemodule);
}
