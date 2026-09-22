class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Start with the last row as the base DP state
        dp = list(triangle[-1])
        
        # Iterate from the second-to-last row up to the top row
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                # The minimum path sum from the current cell to the bottom
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
                
        # The top element now holds the minimum path sum
        return dp[0]
