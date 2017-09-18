/*
 * _consolechange.c.h
 */
#define _CONSOLECHANGE__DOC__ \
"Python extension module that automates" \
" the console (or terminal) title change" \
" stuff for you that works for most (if " \
"not all) platforms in an single python " \
"function (Unlike the multiple ways " \
"people can do it already in python that" \
" requires using sys.platform to get if " \
"it is windows or not just to set it). " \
"This is useful as then it allows much " \
"simpler and platform independent code " \
"without the need to use sys.platform " \
"for any of it just to set an console " \
"(Terminal in unix) title."
#define CONSOLETITLE__DOC__ \
"Sets the console (terminal) title in " \
"a platform independent way."
#define CONSOLESIZE__DOC__ \
"Sets the console size. On Windows " \
"this resizes the console, on any " \
"other platforms it just returns None."

void _change_title(const char *title) {
#if defined(_WIN32)
  SetConsoleTitleA(title);
#elif defined(__linux__) || defined(__CYGWIN__)
  printf("\033]2;%s\007\n\033[1A", title);
#else
  printf("\033]0;%s\007", title);
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
