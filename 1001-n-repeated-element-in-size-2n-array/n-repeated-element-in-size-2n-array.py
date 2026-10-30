class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        # Check elements with a distance gap of 1, 2, or 3
        for gap in range(1, 4):
            for i in range(gap, len(nums)):
                if nums[i] == nums[i - gap]:
                    return nums[i]
                    
        return -1
