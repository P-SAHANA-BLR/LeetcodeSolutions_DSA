from typing import List
from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: The window size is the entire array size
        if k == n:
            return max(nums)
            
        counts = Counter(nums)
        
        # Case 2: Window size is 1
        if k == 1:
            # Find the maximum element that appears exactly once globally
            ans = -1
            for num, count in counts.items():
                if count == 1:
                    ans = max(ans, num)
            return ans
            
        # Case 3: 1 < k < n
        # Only the first or last elements can belong to exactly one subarray.
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans
