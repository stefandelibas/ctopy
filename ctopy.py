from setuptools import setup
import argparse
import subprocess
import sys
import os
import shutil
import glob

debug = True

def clean():
    shutil.rmtree("Release")
    shutil.rmtree("__pycache__")
    os.remove("cffi_module.c")

def get_c(headers, sources):
    cmd = [sys.executable , 'build_cffi.py', "--inc"," ".join(headers), "--src", " ".join(sources)]
    proc = subprocess.Popen(" ".join(cmd))

    while proc.poll() is None:
        # stalling until process is done
        pass

    #import only after the build is done
    import build_py_wrapper 
    mw = build_py_wrapper.get_pywrap()

    if not debug:
        clean()

    return mw

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--inc', type=str, nargs='+', required=True,
                        help='path to H header files.')
    parser.add_argument('--src', type=str, nargs='+', required=True,
                        help='path to C source files.')
    parser.add_argument('-d', default=False, action="store_true",
                        help='Debug flag. keep all intermediary files')
    args = parser.parse_args()

    if args.d:
        debug = args.d
    get_c(args.inc, args.src)