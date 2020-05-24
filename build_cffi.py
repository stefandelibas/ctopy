import argparse
import os
import cffi


ffi = cffi.FFI()

def build_cffi(h_file_names, c_file_names):
    all_h_content = []
    all_c_content = []

    for idx in range(len(args.inc)):
        with open(h_file_names[idx]) as h_file:
            all_h_content.append(h_file.read())

        with open(c_file_names[idx]) as c_file:
             all_c_content.append(c_file.read())
 

    ffi.cdef("\n".join(all_h_content))
    ffi.set_source("cffi_module", "\n".join(all_c_content))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--inc', type=str, nargs='+', required=True,
                        help='path to H header files.')
    parser.add_argument('--src', type=str, nargs='+', required=True,
                        help='path to C source files.')
    args = parser.parse_args()
    
    for idx in range(len(args.inc)):
        if not os.path.exists(args.inc[idx]):
            raise Exception("header file path is incorrect")

        if not os.path.exists(args.src[idx]):
            raise Exception("source file path is incorrect")

    build_cffi(args.inc, args.src)

    ffi.compile(verbose=True)

