import ctypes
import os


def p0030():
    file_path_str = os.path.realpath(__file__)
    path_str = os.path.dirname(file_path_str)

    libc = ctypes.cdll.LoadLibrary(path_str + "/p0030.so")
    r = libc.compute()
    return r
