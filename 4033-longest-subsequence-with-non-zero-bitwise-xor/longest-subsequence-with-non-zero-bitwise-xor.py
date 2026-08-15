from functools import reduce
from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # Calculate the total bitwise XOR of all elements in the array
        total_xor = reduce(lambda x, y: x ^ y, nums, 0)
        
        # Case 1: Total XOR is already non-zero. Keep the entire array.
        if total_xor != 0:
            return len(nums)
        
        # Case 2: Total XOR is zero, but there is at least one non-zero element.
        # Removing any single non-zero element flips the total XOR to non-zero.
        if any(nums):
            return len(nums) - 1
            
        # Case 3: All elements are zero. No non-zero subsequence can be formed.
        return 0
