class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Arrays to store the total number of servers in each row and column
        row_counts = [0] * m
        col_counts = [0] * n
        
        # Step 1: Count how many servers are in each row and column
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
        
        communicating_servers = 0
        
        # Step 2: Check each server to see if it can communicate
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # If there's more than 1 server in its row or its column, it can communicate
                    if row_counts[r] > 1 or col_counts[c] > 1:
                        communicating_servers += 1
                        
        return communicating_servers
