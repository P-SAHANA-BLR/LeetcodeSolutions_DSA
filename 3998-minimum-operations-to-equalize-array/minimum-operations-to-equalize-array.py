from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Check if all elements in the array are equal
        # using a set to count unique values
        if len(set(nums)) == 1:
            return 0
        
        # If there are different elements, we can equalize
        # the entire array in 1 operation.
        return 1
