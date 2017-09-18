/*
 * _consolechange.c.h
 */

static PyObject *consoletitle(PyObject *self, PyObject *args);
static PyObject *consolesize(PyObject *self, PyObject *args);

static PyMethodDef _consolechange_methods[] = {
  {"consoletitle", consoletitle, METH_VARARGS,
   "Sets the console (terminal) title in "
   "a platform independent way."},
  {"consolesize", consolesize, METH_VARARGS,
   "Sets the console size. On Windows "
   "this resizes the console, on any "
   "other platforms it just returns None."},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef _consolechangemodule = {
  PyModuleDef_HEAD_INIT, "_consolechange",
  "Python extension module that automates"
  " the console (or terminal) title change"
  " stuff for you that works for most (if "
  "not all) platforms in an single python "
  "function (Unlike the multiple ways "
  "people can do it already in python that"
  " requires using sys.platform to get if "
  "it is windows or not just to set it). "
  "This is useful as then it allows much "
  "simpler and platform independent code "
  "without the need to use sys.platform "
  "for any of it just to set an console "
  "(Terminal in unix) title.", -1,
  _consolechange_methods
};
