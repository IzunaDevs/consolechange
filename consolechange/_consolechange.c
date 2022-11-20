#include <Python.h>
#include <stdio.h>
#ifdef _WIN32
#include <windows.h>
#endif

static PyObject *
consoletitle(PyObject *self, PyObject *args)
{
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

/* static PyObject *
 * consolesize(PyObject *self, PyObject *args)
 * {
 * #if defined(_WIN32)
 *   int rows, cols;
 *   if (!PyArg_ParseTuple(args, "ii", &rows, &cols))
 *       return NULL;
 *   char buffer [256];
 *   snprintf(buffer, sizeof(buffer),
 *     "mode con: cols=%i lines=%i", rows, cols);
 *   system(buffer);
 * #endif
 *   Py_RETURN_NONE;
 * }
 */

static PyMethodDef _consolechange_methods[] = {
  {"consoletitle", consoletitle, METH_VARARGS,
   "Sets the console (terminal) title in "
   "a platform independent way."},
  /* {"consolesize", consolesize, METH_VARARGS,
   * "Sets the console size. On Windows "
   * "this resizes the console, on any "
   * "other platforms it just returns None."},
   */
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

PyMODINIT_FUNC
PyInit__consolechange(void)
{
  PyObject* m;
  
  m = PyModule_Create(&_consolechangemodule);
  if (m == NULL)
    return NULL;
  
  PyObject *_all_members = PyList_New(2);
  if (_all_members == NULL)
    return NULL;
  
  PyList_SetItem(
    _all_members, 0,
    PyUnicode_FromString("consoletitle"));
  /*
   * PyList_SetItem(
   *   _all_members, 1,
   *   PyUnicode_FromString("consolesize"));
   */
  
  /* expose this here...
   * only needed for travis.
   */
  PyModule_AddObject(m, "all_members", _all_members);
  
  return m;
}
