from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all integers to strings
        num_strs = [str(num) for num in nums]
        
        # Custom comparator function
        def compare(x: str, y: str) -> int:
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1   # y should come before x
            else:
                return 0
        
        # Sort using the custom sorting key
        num_strs.sort(key=cmp_to_key(compare))
        
        # Join the sorted strings
        result = "".join(num_strs)
        
        # Edge case: If the largest number is "0" (e.g., input was [0, 0]), return "0"
        return "0" if result[0] == "0" else result
