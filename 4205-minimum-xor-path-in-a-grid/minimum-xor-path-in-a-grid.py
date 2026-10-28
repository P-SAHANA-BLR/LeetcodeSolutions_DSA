class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # dp[j] stores the set of all possible XOR values reachable at column j 
        # for the current row we are processing
        dp = [set() for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if i == 0 and j == 0:
                    # Starting cell
                    dp[j] = {val}
                elif i == 0:
                    # Top row: can only come from the left
                    dp[j] = {x ^ val for x in dp[j-1]}
                elif j == 0:
                    # Leftmost column: can only come from above
                    dp[j] = {x ^ val for x in dp[j]}
                else:
                    # General cell: can come from either above (dp[j]) or left (dp[j-1])
                    dp[j] = {x ^ val for x in (dp[j-1] | dp[j])}
                    
        # Return the minimum XOR sum achieved at the bottom-right corner
        return min(dp[n-1])


