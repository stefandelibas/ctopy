# cffi_test.py
import cffi_module.lib as lib
from functools import wraps 
import inspect
import types

verbose = False

def add_method(cls):
    def decorator(func):
        @wraps(func) 
        def wrapper(self, *args, **kwargs): 
            return func(*args, **kwargs)
        setattr(cls, func.__name__, wrapper)
        return func
    return decorator


class MemberWrapper:
    def __init__(self):
        pass

    def def_member(self, name, var, var_type):
        self.__setattr__(name, var_type(var))

    def def_method(self, name):
        self.__setattr__(name)
        
    def __str__(self):
        out = ""
        for elem in vars(self):
            out += elem + "=" + str(self.__getattribute__(elem))  + "\ttype=" + str(type(self.__getattribute__(elem))) + "\n"
        return out

def get_pywrap():
    mw = MemberWrapper()
    members = inspect.getmembers(lib)

    if verbose:
        print(members)
    for member in members:
        name, var = member
        if type(var) is types.BuiltinFunctionType:
            if verbose:
                print("it is a builtin_function_or_method")

            func = getattr(lib, str(name))
            setattr(mw, name, func)

        if type(var) in [int, str, float, bytes]:
            if verbose:
                print("{} it is a {}".format(name, type(var)))
            mw.def_member(name, var, type(var))
        else:
            if verbose:
                print("it is a custom data type defined by cffi")
    return mw

if __name__ == "__main__":
    # x, y = 6, 2.3
    # y = example.lib.y 
    # answer = example.lib.cmult(x, y)
    # print("In Python: int: {} float {} return val {}".format(x,y,answer))
    mw = get_pywrap()
    print(mw)
