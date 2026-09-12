from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        
        def backtrack(first: int):
            # Base case: if all positions are filled, record the permutation
            if first == n:
                result.append(list(nums))
                return
                
            for i in range(first, n):
                # Place the i-th element at the current 'first' position
                nums[first], nums[i] = nums[i], nums[first]
                
                # Recursively complete the permutation for the remaining positions
                backtrack(first + 1)
                
                # Backtrack: swap back to restore the original array configuration
                nums[first], nums[i] = nums[i], nums[first]
                
        backtrack(0)
        return result
