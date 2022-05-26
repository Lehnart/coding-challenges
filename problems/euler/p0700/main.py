def p0700():
    current_eulercoin = 1504170715041707
    mod = 4503599627370517
    lo = current_eulercoin
    hi = current_eulercoin
    som = current_eulercoin
    while lo > 0:
        ne = (lo + hi) % mod
        if ne < lo:
            lo = ne
            som += lo
        else:
            hi = ne
    return som
