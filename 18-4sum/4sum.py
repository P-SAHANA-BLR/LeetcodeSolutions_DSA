class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Early Pruning optimization
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break  # Smallest possible sum exceeds target
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue  # Largest possible sum with current nums[i] is too small
                
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # Early Pruning optimization for the second loop
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                    
                # Two-pointer approach for the remaining two elements
                left = j + 1
                right = n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                        
        return res
