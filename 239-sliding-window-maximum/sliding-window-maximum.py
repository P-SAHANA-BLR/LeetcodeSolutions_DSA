from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()  # Will store indices of elements
        res = []
        
        for i, num in enumerate(nums):
            # 1. Remove indices that are out of the current window bound
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # 2. Maintain monotonic decreasing order in the deque
            while q and nums[q[-1]] <= num:
                q.pop()
                
            # Add current element's index
            q.append(i)
            
            # 3. Append the max element to the result once the first window is complete
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res
