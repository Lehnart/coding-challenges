import os

f = open("cypher.txt", "r")
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
            if "chapter" in text:
                som = 0
                for c in text:
                    som += ord(c)
                print("Solution : " + str(som))
                os._exit(0)
