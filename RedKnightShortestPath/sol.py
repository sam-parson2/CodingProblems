def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Append moves to a list and print from that list, BFS explore all possible paths I guess,  first to get there is probably the shorted path
    moves = {
        "UL": (-2, -1),
        "UR": (-2, +1),
        "R" : ( 0, +2),
        "LR": (+2, +1),
        "LL": (+2, -1),
        "L" : ( 0, -2),
    }
    from collections import deque
    queue = deque([[[i_start, j_start], []]])
    visited = {(i_start, j_start)}
    while queue:
        cur_position, hist = queue.popleft()
        if [cur_position[0], cur_position[1]] == [i_end, j_end]:
            print(len(hist))
            print(*hist)
            return
        
        for state, move in moves.items():
            tenative = [move[i] + cur_position[i] for i in range(2)]
            if max(tenative) <= n - 1 and all(idx >= 0 for idx in tenative) \
            and tuple(tenative) not in visited:
                visited.add(tuple(tenative))
                new_hist = hist + [state]
                queue.append([[*tenative], new_hist])
             
    print('Impossible')