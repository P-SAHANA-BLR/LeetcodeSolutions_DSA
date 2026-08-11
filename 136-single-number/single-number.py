from functools import reduce
from operator import xor
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Reduce applies the XOR operator sequentially to all elements in the list
        return reduce(xor, nums)
