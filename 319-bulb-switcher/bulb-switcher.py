import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # The number of bulbs that remain ON is exactly the number of 
        # perfect squares less than or equal to n.
        return int(math.isqrt(n))
