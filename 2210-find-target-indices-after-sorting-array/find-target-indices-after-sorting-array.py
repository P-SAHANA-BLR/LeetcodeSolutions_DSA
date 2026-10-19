class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less_than_target = 0
        equal_to_target = 0
        
        # Count elements in a single pass
        for num in nums:
            if num < target:
                less_than_target += 1
            elif num == target:
                equal_to_target += 1
        
        # Generate the sorted indices
        return [i for i in range(less_than_target, less_than_target + equal_to_target)]
