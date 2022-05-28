import ctypes
import os


def p0034():
    file_path_str = os.path.realpath(__file__)
    path_str = os.path.dirname(file_path_str)
    libc = ctypes.cdll.LoadLibrary(path_str +"/p0034.so")
    result = libc.compute()
    return result

