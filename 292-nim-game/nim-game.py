class Solution:
    def canWinNim(self, n: int) -> bool:
        # You will lose if and only if the number of stones is a multiple of 4
        return n % 4 != 0
