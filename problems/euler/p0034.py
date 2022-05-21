import ctypes


def algo():
    libc = ctypes.cdll.LoadLibrary("./p0034.so")
    result = libc.compute()
    return result


if __name__ == "__main__":
    import cProfile

    cProfile.run("algo()")
