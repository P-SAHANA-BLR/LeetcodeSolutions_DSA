from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        
        # If the start or end is unreachable/invalid directly
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0
            
        # destination[i][j][d] stores (next_i, next_j, next_dir)
        # d = 0 means entered moving Right, d = 1 means entered moving Down
        destination = [[ [(-1, -1, -1)] * 2 for _ in range(n) ] for _ in range(m)]
        
        # Resolve destination for every cell and entry direction bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 1. Entering (i, j) moving Right (d = 0)
                if grid[i][j] == 0:
                    destination[i][j][0] = (i, j, 0)
                else: # Mirror: turns down to (i + 1, j)
                    if i + 1 < m:
                        destination[i][j][0] = destination[i + 1][j][1]
                    else:
                        destination[i][j][0] = (-1, -1, -1) # Out of bounds
                        
                # 2. Entering (i, j) moving Down (d = 1)
                if grid[i][j] == 0:
                    destination[i][j][1] = (i, j, 1)
                else: # Mirror: turns right to (i, j + 1)
                    if j + 1 < n:
                        destination[i][j][1] = destination[i][j + 1][0]
                    else:
                        destination[i][j][1] = (-1, -1, -1) # Out of bounds

        # dp[i][j][d]: paths from (i, j) to (m-1, n-1) after safely arriving at (i, j) with direction d
        dp = [[ [0] * 2 for _ in range(n) ] for _ in range(m)]
        
        # Base case: Already successfully arrived at the destination cell
        dp[m - 1][n - 1][0] = 1
        dp[m - 1][n - 1][1] = 1
        
        # Populate DP table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    continue
                if i == m - 1 and j == n - 1:
                    continue
                    
                # From non-mirror cell (i, j), we have two choices for the next move:
                
                # Choice 1: Move Right into (i, j + 1)
                if j + 1 < n:
                    ni, nj, nd = destination[i][j + 1][0]
                    if ni != -1:
                        # Add paths for both incoming directions to (i, j)
                        dp[i][j][0] = (dp[i][j][0] + dp[ni][nj][nd]) % MOD
                        dp[i][j][1] = (dp[i][j][1] + dp[ni][nj][nd]) % MOD
                        
                # Choice 2: Move Down into (i + 1, j)
                if i + 1 < m:
                    ni, nj, nd = destination[i + 1][j][1]
                    if ni != -1:
                        # Add paths for both incoming directions to (i, j)
                        dp[i][j][0] = (dp[i][j][0] + dp[ni][nj][nd]) % MOD
                        dp[i][j][1] = (dp[i][j][1] + dp[ni][nj][nd]) % MOD
                        
        # At the start (0, 0), the robot can initiate a move either Right or Down.
        # This is equivalent to evaluating choices from a virtual starting state.
        total_paths = 0
        
        # Try moving Right from (0, 0) -> goes to (0, 1) entering moving Right
        if n > 1:
            ni, nj, nd = destination[0][1][0]
            if ni != -1:
                total_paths = (total_paths + dp[ni][nj][nd]) % MOD
                
        # Try moving Down from (0, 0) -> goes to (1, 0) entering moving Down
        if m > 1:
            ni, nj, nd = destination[1][0][1]
            if ni != -1:
                total_paths = (total_paths + dp[ni][nj][nd]) % MOD
                
        return total_paths
