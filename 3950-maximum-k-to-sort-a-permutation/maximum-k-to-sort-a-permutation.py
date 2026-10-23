from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Initialize ans to -1 (in Python, bitwise AND with -1 acts as an all-1s mask)
        ans = -1
        
        # Iterate through the permutation with its indices
        for i, x in enumerate(nums):
            # Track and accumulate the bitwise AND of all misplaced elements
            if i != x:
                ans &= x
                
        # If the array was already sorted, ans remains -1, so we return 0.
        # Otherwise, we return the maximum valid k.
        return max(ans, 0)
