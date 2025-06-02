def quickestWayUp(ladders, snakes):
    from collections import deque
    shifts = {x[0]: x[1] for x in [*ladders, *snakes]}
    moves = {x for x in range(1, 7)}
    visited = {1}
    q = deque([(1, 0)])
    while q:
        pos, count = q.popleft()
        if pos == 100:
            return count
        for move in moves:
            candidate = pos + move
            if candidate in shifts:
                candidate = shifts[candidate]
            if candidate in visited or candidate > 100:
                continue
            visited.add(candidate)
            q.append((candidate, count + 1)) 
    return -1