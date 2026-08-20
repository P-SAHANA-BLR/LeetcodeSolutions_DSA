class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. Replace negative numbers, zeros, and numbers > n with n + 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
                
        # 2. Use indices as a hash map by flipping signs to negative
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                # Map the number to its corresponding 0-based index
                idx = num - 1
                nums[idx] = -abs(nums[idx])
                
        # 3. Find the first index that contains a positive number
        for i in range(n):
            if nums[i] > 0:
                return i + 1
                
        # 4. If numbers 1 to n are all present, the missing one is n + 1
        return n + 1
