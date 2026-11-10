class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        # Initialize variables for Kadane's algorithm
        total_sum = 0
        
        curr_max = 0
        max_sum = nums[0]
        
        curr_min = 0
        min_sum = nums[0]
        
        for num in nums:
            total_sum += num
            
            # Standard Kadane's to find maximum subarray sum
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            
            # Modified Kadane's to find minimum subarray sum
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
            
        # If max_sum is negative, all elements are negative.
        # In this case, total_sum == min_sum, so total_sum - min_sum would be 0 (invalid empty array).
        # We must return the maximum single element instead.
        if max_sum < 0:
            return max_sum
            
        return max(max_sum, total_sum - min_sum)
