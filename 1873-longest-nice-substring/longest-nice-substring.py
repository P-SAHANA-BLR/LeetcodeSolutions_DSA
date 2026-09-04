class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        char_set = set(s)
        
        for i, char in enumerate(s):
            # If a character's counterpart is missing, it breaks the string
            if char.swapcase() not in char_set:
                # Divide the string into left and right subproblems
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                
                # Return the longer one (if lengths are equal, left takes priority for earliest occurrence)
                if len(left) >= len(right):
                    return left
                return right
                
        # If no violating character was found, the whole string is nice
        return s
