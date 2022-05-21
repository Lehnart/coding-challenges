def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    return a ** 2 + b ** 2 == c ** 2


def p0009(s: int = 1000):
    for a in range(1, s):
        for b in range((s // 2) - a, s):
            for c in range(b, (s // 2)):
                if a + b + c < s:
                    continue

                if a + b + c > s:
                    break

                if is_pythagorean_triplet(a, b, c) and a + b + c == s:
                    return a * b * c
