from collections import Counter
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = Counter()
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            right_num = nums[right]
            frequency[right_num] += 1
            
            # Shrink window from the left if the current element's frequency exceeds k
            while frequency[right_num] > k:
                frequency[nums[left]] -= 1
                left += 1
                
            # Update the maximum length of a valid window
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                
        return max_length
