class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # Shift result left and add the rightmost bit of n
            result = (result << 1) | (n & 1)
            # Shift n right to process the next bit
            n >>= 1
        return result
