
def journeyToMoon(n, astronaut):
    import sys
    sys.setrecursionlimit(5000) 
    if n in [0, 1]:
        return 0
    from collections import defaultdict
    pairs = 0
    visited = set()
    graph = defaultdict(list)
    for i, j in astronaut:
        graph[i].append(j)
        graph[j].append(i)
    
    def dfs(i):
        visited.add(i)
        size = 1
        for u in graph[i]:
            if u not in visited:
                size += dfs(u)
        return size
        
    components = []
    for i in range(n):
        if i not in visited:
                components.append(dfs(i))
    cumulative = sum(components)
    
    for j in range(len(components)):
        cumulative -= components[j]
        pairs += components[j] * cumulative

    return pairs