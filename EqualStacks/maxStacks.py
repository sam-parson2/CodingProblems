def equalStacks(h1, h2, h3):
    if not h1 or not h2 or not h3:
        return 0
    acc = 0
    l = {acc := x + acc for x in reversed(h1)}; acc = 0
    m = {acc := x + acc for x in reversed(h2)}; acc = 0
    h = {acc := x + acc for x in reversed(h3)}; acc = 0
    intersection = l & m & h
    return max(intersection) if intersection else 0