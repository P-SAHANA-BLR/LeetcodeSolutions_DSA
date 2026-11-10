class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[i] will store the minimum cost to reach step i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Starting at step 0 has 0 cost
        
        for i in range(1, n + 1):
            # We can reach step i from step i-1, i-2, or i-3
            for k in range(1, 4):
                if i - k >= 0:
                    # costs is 1-indexed in the problem, so step i uses costs[i-1]
                    jump_cost = costs[i - 1] + (k ** 2)
                    dp[i] = min(dp[i], dp[i - k] + jump_cost)
                    
        return dp[n]

