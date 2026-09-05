class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        # Keep checking as long as the repeated word is a substring of sequence
        while (word * (k + 1)) in sequence:
            k += 1
            
        return k
