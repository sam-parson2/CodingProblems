def minimumMoves(grid, startX, startY, goalX, goalY):
    def generateLegalMoves(cur_x, cur_y):
        validmoves = {(-1, 0), (1, 0), (0, 1), (0, -1)}
        moves = []
        for dx, dy in validmoves:
            nx, ny = cur_x + dx, cur_y + dy
            while 0 <= nx < len(grid) and 0 <= ny < len(grid) \
            and grid[nx][ny] != "X":
                moves.append((nx, ny))
                nx += dx
                ny += dy
        return {*moves}
                
    from collections import deque # O(1) left pop
    q = deque([(startX, startY, 0)])
    visited = {(startX, startY)}
    while q:
        next_element = q.popleft()
        x, y, steps = next_element
        if (x, y) == (goalX, goalY):
            return steps 
        for nx, ny in generateLegalMoves(x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, steps + 1))
    return -1