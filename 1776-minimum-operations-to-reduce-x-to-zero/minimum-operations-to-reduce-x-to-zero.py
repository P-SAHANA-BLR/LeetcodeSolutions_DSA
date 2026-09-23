class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        
        # If the target is exactly 0, we must remove all elements
        if target == 0:
            return len(nums)
        
        # If the target is negative, it's impossible to sum up to x
        if target < 0:
            return -1
        
        max_len = -1
        current_sum = 0
        left = 0
        
        # Sliding window to find the longest subarray summing up to target
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window from the left if the current sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # Check if we hit the target sum exactly
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        # If max_len was updated, return remaining elements; else return -1
        return len(nums) - max_len if max_len != -1 else -1
