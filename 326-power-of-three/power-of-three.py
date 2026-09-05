class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 1162261467 is 3^19, the maximum power of 3 within a 32-bit signed integer
        return n > 0 and 1162261467 % n == 0
