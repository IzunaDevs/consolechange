#include "_consolechange.c.h"

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

static PyObject *
consolesize(PyObject *self, PyObject *args) {
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
