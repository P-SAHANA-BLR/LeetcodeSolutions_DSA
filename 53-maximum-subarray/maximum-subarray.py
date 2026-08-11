class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize both the running sum and global maximum with the first element
        max_so_far = nums[0]
        current_max = nums[0]
        
        # Iterate through the rest of the array starting from index 1
        for i in range(1, len(nums)):
            # Decide whether to extend the existing subarray or start a new one
            current_max = max(nums[i], current_max + nums[i])
            # Update the global maximum subarray sum found so far
            max_so_far = max(max_so_far, current_max)
            
        return max_so_far
