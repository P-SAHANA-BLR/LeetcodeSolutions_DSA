class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        # Iterate through both strings
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        # If i reached the end of s, then s is a subsequence of t
        return i == len(s)
