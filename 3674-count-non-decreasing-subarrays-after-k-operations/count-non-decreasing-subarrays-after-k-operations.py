from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0
        r = n - 1
        
        # Monotonic decreasing deque storing pairs of [value, count]
        # Represents the step-function of running maximums from l to r
        dq = deque()
        
        for l in range(n - 1, -1, -1):
            curr_val = nums[l]
            count = 1
            
            # Merge all elements to the right that are smaller than or equal to nums[l]
            while dq and dq[0][0] <= curr_val:
                val, cnt = dq.popleft()
                # Increasing 'cnt' elements from 'val' up to 'curr_val'
                cost += (curr_val - val) * cnt
                count += cnt
                
            dq.appendleft([curr_val, count])
            
            # Shrink the window from the right if total operations exceed k
            while cost > k:
                # The rightmost element's required target value is at the back of the deque
                cost -= dq[-1][0] - nums[r]
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1
                
            # All subarrays starting at l and ending between l and r are valid
            ans += (r - l + 1)
            
        return ans
