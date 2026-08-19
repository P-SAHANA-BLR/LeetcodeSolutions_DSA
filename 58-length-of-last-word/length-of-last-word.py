class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split() strips all extra whitespace and splits into a list of words
        words = s.split()
        
        # Return the length of the last element in the list
        return len(words[-1])
