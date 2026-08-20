class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # Step 1: Cyclic Sort - Place each number at its correct index if possible
        for i in range(n):
            # Keep swapping until nums[i] is out of bounds or already at the correct spot
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap elements using Pythonic tuple unpacking
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]

        # Step 2: Find the first index mismatch
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1 # The missing positive number

        # Step 3: If all spots are perfectly filled, the missing number is n + 1
        return n + 1
