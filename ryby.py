def ryby(n, m, b):
    f = []
    w = 0
    for i in range(b):
        if m[i] == 1:
            f.insert(0, n[i])
        else:
            if f:
                o, f = r(f, n[i])
                w += o
            else:
                w += 1
    w += len(f)
    print(w)
    return w


def r(f, n):
    p = f
    for i in f:
        if i < n:
            p.pop(0)
        else:
            return 0, p
    return 1, []


assert ryby([4, 3, 2, 1, 5], [0, 1, 0, 0, 0], 5) == 2
assert ryby([1, 3, 5, 2], [1, 1, 1, 1], 4) == 4
assert ryby([1, 3, 2, 5], [0, 0, 0, 0], 4) == 4
