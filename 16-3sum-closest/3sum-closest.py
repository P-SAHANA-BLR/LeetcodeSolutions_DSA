class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to enable the two-pointer technique
        nums.sort()
        n = len(nums)
        
        # Initialize closest_sum with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find an exact match, return it immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current_sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Adjust pointers based on the comparison with the target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
