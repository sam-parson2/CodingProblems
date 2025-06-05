def connectedCell(matrix):
    max_region = 0
    visited = set() 
    
    # We will never need to recount a cell we have counted before
    # Since in any scenario where that would happen, our DFS
    # Would of counted it as being part of the max_region for some
    # Other starting point
    # In other words, if you are trying to count the number of 
    # Connected cells, it does not matter where you start
    
    valid_moves = {
        (0, 1), # Right
        (0, -1), # Left
        (1, 0), # Down
        (-1, 0), # Up
        (-1, 1), # Top-Right
        (-1, -1), # Top-left
        (1, 1), # Bottom Right
        (1, -1), # Bottom Left
    }
    # DFS
    def dfs(i, j):
        visited.add((i, j))
        size = 1
        for move in valid_moves:
            x, y = (i + move[0]), (j + move[1])
            
            if 0 <= x < len(matrix) and \
            0 <= y < len(matrix[0]) and \
            (x,y) not in visited and matrix[x][y] == 1:
            
                size += dfs(x, y) # Add 1 for each successful DFS
                
        return size # Parent call will acccumulate all 1s
         
    starts = [(i, j)
             for i in range(len(matrix))
             for j in range(len(matrix[0]))
             if matrix[i][j] == 1
             ] # Start DFS from all '1' cells
             
    for idx_pair in starts: # For 1s in grid
        if idx_pair not in visited:
            size = dfs(*idx_pair)
            max_region = max(max_region, size)
            
    return max_region