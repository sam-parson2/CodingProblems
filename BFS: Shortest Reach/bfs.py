def bfs(n, m, edges, s):
    from collections import deque, defaultdict
    graph = defaultdict(list)
    vals = {x: -1 for x in range(1, n + 1) if x != s}
    visited = {s}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    distance = 0
    q = deque([(s, distance)])
    while q:
        current, steps = q.popleft()
        for node in graph[current]:
            if node not in visited:
                visited.add(node)
                vals[node] = steps + 6
                q.append((node, steps + 6))
    return list(vals.values())