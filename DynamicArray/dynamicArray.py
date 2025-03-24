def dynamicArray(n, queries):
    res = []
    XOR = lambda x, y: x ^ y
    compute_last = lambda x, y, last, collection: collection[XOR(x, last) % n][y % len(collection[XOR(x, last) % n])]
    init = [[] for _ in range(n)]
    last_ans = 0
    for k in queries:
        if k[0] == 1:
            init[XOR(k[1], last_ans) % n].append(k[2])
        if k[0] == 2:
            last_ans = compute_last(k[1], k[2], last_ans, init)
            res.append(last_ans)
    return res