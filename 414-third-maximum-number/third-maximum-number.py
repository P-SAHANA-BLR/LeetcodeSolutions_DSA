from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = -float('inf')
        
        for num in nums:
            # Skip duplicates to maintain distinct maximums
            if num in (first, second, third):
                continue
                
            # Update pointers based on the size of the current number
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
                
        # If a third distinct maximum does not exist, return the maximum
        return third if third != -float('inf') else first
