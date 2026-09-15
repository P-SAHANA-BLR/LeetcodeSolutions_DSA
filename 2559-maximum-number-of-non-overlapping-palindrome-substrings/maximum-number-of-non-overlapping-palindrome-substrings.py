class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        # dp[i] stores the max number of non-overlapping palindromes in s[0...i-1]
        dp = [0] * (n + 1)
        
        for i in range(n):
            # Base transition: carrying forward the best result from the previous index
            dp[i + 1] = max(dp[i + 1], dp[i])
            
            # Check for palindromes centered at i (odd length) 
            # and centered between i and i+1 (even length)
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < n and s[l] == s[r]:
                    if r - l + 1 >= k:
                        # If a valid palindrome is found from l to r,
                        # it can extend the max palindromes found up to index l
                        dp[r + 1] = max(dp[r + 1], dp[l] + 1)
                        break  # Greedily stop expanding; shorter valid palindromes leave more space
                    l -= 1
                    r += 1
                    
        return dp[n]
