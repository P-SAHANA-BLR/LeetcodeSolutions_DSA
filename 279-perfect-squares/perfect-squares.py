class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] will store the least number of perfect squares that sum to i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case
        
        # Build the dp array from 1 to n
        for i in range(1, n + 1):
            j = 1
            # Check all perfect squares less than or equal to i
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
                
        return dp[n]
