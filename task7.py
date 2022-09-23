def find_shortest(l: str) -> int:
    c = 0
    a = len(l)
    for x in l:
        if x.isalpha() and x.isascii():
            c += 1
        else:
            a = min(a, c) if c > 0 else a
            c = 0
    if c:
        a = min(a, c)
        return a
    return a if a != len(l) else 0
