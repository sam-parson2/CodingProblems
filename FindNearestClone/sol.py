def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    from collections import deque, defaultdict
    
    graph = defaultdict(list) # Build adjacency list
    for u, v in zip(graph_from, graph_to):
        graph[u].append(v)
        graph[v].append(u)
    # Dict of node: list of connected nodes
    sources = [i + 1 for i, color in enumerate(ids) if color == val]
    # Find the nodes to start searching from
    # Start search only from nodes that are of the target color
    
    if len(sources) < 2:
    # If there are not two nodes of the target color, return -1
        return -1
    
    visited = {}
    q = deque()
    
    for src in sources: 
        visited[src] = (src, 0)
        q.append((src, 0, src)) 
    # (cur_node, distance, source_node)
    
    # Now run BFS
    while q:
        current, dist, origin = q.popleft()
        for n in graph[current]:
            # Check with nodes are connected to our current node
            # Using the adj list
            if n not in visited:
                visited[n] = (origin, dist + 1)
                q.append((n, dist + 1, origin))
            else:
                prev, _ = visited[n]
                # If we can get to node x, from two distinct starting locations
                # We have found the shortest path between those two nodes
                # Since we only start BFS from nodes of the target color
                # We have therefore completed the problem
                if prev != origin:
                    return dist + 1 + visited[n][1]
                # Sum the two weights that we have travelled thus far,
                # Since we basically split the problem in two, we need to sum
                # The two distances, to account for the fact that we are
                # Finding the distance to a mutual node in the middle of
                # The two nodes, rather than purely the distance between the 
                # Two nodes - so add both dists to get the full length of the 
                # Path between them
    return -1 