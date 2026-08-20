class Solution:
    def longestPalindrome(self, s: str) -> int:
        unmatched_chars = set()
        length = 0
        
        for char in s:
            if char in unmatched_chars:
                # We found a pair, add 2 to the length and remove from set
                length += 2
                unmatched_chars.remove(char)
            else:
                # Character is waiting for a match
                unmatched_chars.add(char)
                
        # If there are any unmatched characters left, we can place one in the middle
        if unmatched_chars:
            length += 1
            
        return length
