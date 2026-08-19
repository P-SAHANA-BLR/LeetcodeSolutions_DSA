class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c_counts = {}
        
        # Count how many times each character appears in s
        for char in s:
            if char in c_counts:
                c_counts[char] += 1
            else:
                c_counts[char] = 1
                
        # Check characters in t against our counts
        for char in t:
            # If a character isn't in s, or its count drops below 0,
            # this must be the extra character!
            if char not in c_counts or c_counts[char] == 0:
                return char
            c_counts[char] -= 1
