class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Convert list to a set for O(1) lookups
        word_set = set(wordDict)
        n = len(s)
        
        # dp[i] will be True if s[0:i] can be segmented
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string
        
        # Optimization: Find the length of the longest word in the dictionary
        max_len = max(len(word) for word in wordDict) if wordDict else 0
        
        for i in range(1, n + 1):
            # Check previous split points. 
            # We only look back up to max_len to save unnecessary iterations.
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Found a valid split for s[0:i], no need to check further
                    
        return dp[n]
