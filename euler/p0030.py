import ctypes


def algo():
    libc = ctypes.cdll.LoadLibrary("./p0030.so")
    l = libc.compute()
    return l


if __name__ == "__main__":
    import cProfile

    cProfile.run("algo()")
