def ryby(n, sizes, directions):
    stack = []
    result = 0
    for i in range(directions):
        if sizes[i] == 1:
            stack.append(n[i])
        else:
            if stack:
                result += eat_smaller(stack, n[i])
            else:
                result += 1
    result += len(stack)
    return result


def eat_smaller(f, n):
    for i in f:
        if i < n:
            f.pop()
        else:
            return 0
    return 1


assert ryby([4, 3, 2, 1, 5], [0, 1, 0, 0, 0], 5) == 2
assert ryby([1, 3, 5, 2], [1, 1, 1, 1], 4) == 4
assert ryby([1, 3, 2, 5], [0, 0, 0, 0], 4) == 4
