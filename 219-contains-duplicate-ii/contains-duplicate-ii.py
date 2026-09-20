from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}  # Maps number -> its most recent index
        
        for i, num in enumerate(nums):
            
            # If the number was seen before and is within the distance 'k'
            if num in seen and i - seen[num] <= k:
                return True
            
            # Update the index of the current number
            seen[num] = i
            
        return False