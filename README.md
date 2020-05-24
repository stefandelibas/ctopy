# ctopy
Python library that maps C object to python objects

To use this module you need to have a list of C source files and a list of H header files as input.
After calling ctopy.get_c(...) you will get a member wrapper of the C variables and method.

An example can be seen in main.py



Refs:
https://cffi.readthedocs.io/en/latest/overview.html#main-mode-of-usage
https://realpython.com/python-bindings-overview/#cffi