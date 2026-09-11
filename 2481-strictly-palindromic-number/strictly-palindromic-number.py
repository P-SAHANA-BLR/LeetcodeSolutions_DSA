class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # It is mathematically impossible for any n >= 4 
        # to be a palindrome in base n - 2.
        return False
