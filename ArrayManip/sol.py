def arrayManipulation(n, queries):
    base = [0] * (n + 2)
    for x in queries:
        base[x[0]] += x[2]
        base[x[1] + 1] -= x[2]
    mx, acc = 0, 0
    for i, val in enumerate(base):
        acc += val
        mx = max(acc, mx)
    return mx