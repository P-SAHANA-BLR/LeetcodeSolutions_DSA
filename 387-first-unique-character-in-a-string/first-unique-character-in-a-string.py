from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Pass 1: Build the frequency map of all characters
        counts = Counter(s)
        
        # Pass 2: Iterate through the string to find the first character with a count of 1
        for idx, ch in enumerate(s):
            if counts[ch] == 1:
                return idx
                
        # If no unique character is found, return -1
        return -1
