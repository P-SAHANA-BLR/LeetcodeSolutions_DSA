class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Calculate the sum of the longest sequential prefix
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
                
        # Step 2: Convert nums to a set for O(1) lookups
        num_set = set(nums)
        
        # Step 3: Increment prefix_sum until we find a value missing from the set
        while prefix_sum in num_set:
            prefix_sum += 1
            
        return prefix_sum
