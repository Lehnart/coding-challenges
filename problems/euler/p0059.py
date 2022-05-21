def algo():
    f = open("p0059_cypher.txt", "r")
    lines = f.readline()
    numbers = [int(c) for c in lines.split(",")]

    chars = "abcdefghijklmnopqrstuvwxyz"
    for c1 in chars:
        for c2 in chars:
            for c3 in chars:
                cs = [ord(c1), ord(c2), ord(c3)]
                text = ""
                i = 0
                for n in numbers:
                    text += chr(n ^ cs[i % 3])
                    i += 1
                if "the" in text and "that" in text:
                    som = 0
                    for c in text:
                        som += ord(c)
                    f.close()
                    return som
