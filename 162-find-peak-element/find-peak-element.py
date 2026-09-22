class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # If we are climbing upwards towards the right, the peak is to the right
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            # If we are dropping downwards towards the right, the peak is to the left or at mid
            else:
                high = mid
                
        return low
