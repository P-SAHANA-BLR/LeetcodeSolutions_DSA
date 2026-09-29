class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # Base case: If the starting or ending cell is an obstacle, no paths exist
        if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # DP array to track paths for the current row
        dp = [0] * n
        dp[0] = 1 # Base case: 1 way to be at the starting point
        
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0 # Obstacle blocks all paths to this cell
                elif c > 0:
                    # Current cell paths = paths from above (dp[c]) + paths from left (dp[c-1])
                    dp[c] += dp[c-1]
                    
        return dp[n-1]
