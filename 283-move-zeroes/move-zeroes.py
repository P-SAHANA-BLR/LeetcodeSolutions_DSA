class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Pointer to track where the next non-zero element should go
        last_non_zero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                # Only perform a swap if the pointers are at different positions.
                # This avoids redundant self-swapping operations for arrays with no zeroes.
                if i != last_non_zero:
                    nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1
