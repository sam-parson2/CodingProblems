import math
from collections import deque

def downToZero(n):
    queue = deque([(n, 0)])
    visited = {n}

    while queue:
        cur, moves = queue.popleft()
        if cur == 0:
            return moves
    
        # Sub 1
        nxt = cur - 1
        if nxt not in visited:
            visited.add(nxt)
            queue.append((nxt, moves + 1))
    
        lim = int(math.sqrt(cur))
        for i in range(2, lim + 1):
            if cur % i == 0:
                alt = max(i, cur // i)
                if alt not in visited:
                    visited.add(alt)
                    queue.append((alt, moves + 1))
    return -1 


        
