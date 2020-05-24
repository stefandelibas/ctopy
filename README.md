# ctopy
Python library that maps C object to python objects

To use this module you need to have a list of C source files and a list of H header files as input.
After calling ctopy.get_c(...) you will get a member wrapper of the C variables and method.

An example can be seen in main.py

build_cffi will build a dynamic python library (pyd) that can be used as standalone library too.
build_py_wrapper will read the pyd and map mathods and variables. it will build an object that wrapps all components
ctopy is the module that controls everythoing

Requirments:
	- python 3.x
	- cffi (this module can be installed with pip)
	- MSVC 14+ building tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/

Refs:
https://cffi.readthedocs.io/en/latest/overview.html#main-mode-of-usage
https://realpython.com/python-bindings-overview/#cffi