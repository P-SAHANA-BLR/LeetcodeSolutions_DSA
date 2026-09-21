class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Initialize DP table for the first row
        dp = [0] * n
        dp[0] = grid[0][0]
        
        # Pre-fill the first row since you can only come from the left
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
            
        # Compute the rest of the rows
        for i in range(1, m):
            # For the first element of a row, you can only come from above
            dp[0] += grid[i][0]
            
            # For the rest of the elements, choose the minimum between coming from above or left
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
                
        return dp[-1]
