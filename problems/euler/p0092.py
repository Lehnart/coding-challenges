import ctypes


def algo():
    libc = ctypes.cdll.LoadLibrary("./p0092.so")
    result = libc.compute()
    return result


if __name__ == "__main__":
    algo()
    # import cProfile
    # cProfile.run("algo()")
