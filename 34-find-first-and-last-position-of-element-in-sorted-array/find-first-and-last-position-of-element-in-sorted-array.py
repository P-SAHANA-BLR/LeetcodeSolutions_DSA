import bisect

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # bisect_left finds the first index where target could be inserted to maintain order
        left = bisect.bisect_left(nums, target)
        
        # If left is out of bounds or the element at left is not the target
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
            
        # bisect_right finds the insertion point after any existing targets
        right = bisect.bisect_right(nums, target) - 1
        
        return [left, right]
