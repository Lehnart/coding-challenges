def split(a, n):
    """
    split list in almost equal length sublists
    @param a : list to split
    @param n : number of sublists.
    """
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))
