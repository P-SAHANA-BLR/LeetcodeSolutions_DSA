class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # The sum of differences between each element and the minimum element
        return sum(nums) - len(nums) * min(nums)
