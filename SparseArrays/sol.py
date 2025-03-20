def matchingStrings(stringList, queries):
    res = {x: 0 for x in queries}
    for y in stringList:
        if y in res:
            res[y] += 1
    return [res.get(x) for x in queries]