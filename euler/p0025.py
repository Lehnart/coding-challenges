def algo():
    current = 2
    prev = 1
    index = 3
    while True:
        current, prev = (current + prev, current)
        index += 1
        if len(str(current)) >= 1000:
            return index
