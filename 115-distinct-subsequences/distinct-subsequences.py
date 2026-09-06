class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] will store the number of distinct subsequences for t[:j]
        # We optimize space to 1D since we only need the previous row's data.
        dp = [0] * (n + 1)
        
        # Base case: An empty string t is a subsequence of any prefix of s in exactly 1 way.
        dp[0] = 1
        
        # Iterate through each character of s
        for i in range(1, m + 1):
            # Iterate backwards through t to use values from the previous 'i' iteration
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    # Current count = (count without using s[i-1]) + (count using s[i-1])
                    dp[j] = dp[j] + dp[j - 1]
                # If they don't match, dp[j] remains the same (dp[j] from previous s character)
                
        return dp[n]
