def missingNumbers(arr, brr):
    if not arr:
        return sorted(list(brr.keys()))
    if not brr:
        return sorted(list(arr.keys()))
        
    def createCounter(collection):
        freqs = {}
        for x in collection:
            if x in freqs:
                freqs[x] += 1
            else:
                freqs[x] = 1
        return freqs
    def checkEquality(a, b):
        missing_vals = []
        for k in sorted(list(b.keys())):
            if k not in a:
                missing_vals.append(k)
            else:
                if b[k] != a[k]:
                    missing_vals.append(k)
        for left_over in list(a.keys()):
            if left_over not in missing_vals and left_over not in b:
                missing_vals.append(left_over)
        return missing_vals
    base, missing = createCounter(brr), createCounter(arr)
    res = checkEquality(missing, base)

    return res
