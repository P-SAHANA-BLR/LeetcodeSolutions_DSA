from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the current width
            width = right - left
            
            # The height of the container is limited by the shorter line
            current_height = min(height[left], height[right])
            
            # Calculate current water capacity and update max_water if it's larger
            current_water = width * current_height
            if current_water > max_water:
                max_water = current_water
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
