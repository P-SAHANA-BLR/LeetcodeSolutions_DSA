class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if s[0...i-1] matches p[0...j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: Empty string matches empty pattern
        dp[0][0] = True
        
        # Base cases: Deal with patterns like a*, a*b*, a*b*c* matching empty string s
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # Current characters match, inherit status from diagonal upper-left
                    dp[i][j] = dp[i - 1][j - 1]
                    
                elif p[j - 1] == '*':
                    # Case 1: '*' matches zero occurrences of the preceding character
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case 2: '*' matches one or more occurrences
                    # The preceding pattern character must match the current string character
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]
