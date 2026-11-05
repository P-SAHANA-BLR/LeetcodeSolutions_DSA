class NumArray:

    def __init__(self, nums: list[int]):
        # Create a prefix sum array padded with an extra 0 at the start.
        # self.prefix_sums[i] will store the sum of nums[0] up to nums[i-1].
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # The sum from left to right inclusive is equivalent to:
        # (sum from index 0 to right) - (sum from index 0 to left - 1)
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
