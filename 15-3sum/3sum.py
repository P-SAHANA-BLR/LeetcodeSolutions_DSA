class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 2):
            # If the smallest number in the triplet is greater than 0, 
            # the sum can never be 0.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return res
