class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A power of two must be positive and have exactly one bit set to 1
        return n > 0 and (n & (n - 1)) == 0
