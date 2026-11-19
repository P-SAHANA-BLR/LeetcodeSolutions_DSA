from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        
        return min(
            nums[-1] - nums[2],   # Remove 2 smallest
            nums[-3] - nums[0],   # Remove 2 largest
            nums[-2] - nums[1]    # Remove 1 smallest and 1 largest
        )
