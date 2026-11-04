from typing import List
from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
        # cost[i] stores the min operations to make nums[i:i+x] equal
        cost = [0] * (n - x + 1)
        
        left = SortedList()
        right = SortedList()
        left_sum = 0
        right_sum = 0
        
        left_target_size = (x + 1) // 2
        
        def balance():
            nonlocal left_sum, right_sum
            # If left has too many elements, move the largest to right
            while len(left) > left_target_size:
                val = left.pop()
                left_sum -= val
                right.add(val)
                right_sum += val
            # If left has too few elements, move the smallest from right
            while len(left) < left_target_size and right:
                val = right.pop(0)
                right_sum -= val
                left.add(val)
                left_sum += val

        # Initialize the first window
        for i in range(x):
            val = nums[i]
            if right and val >= right[0]:
                right.add(val)
                right_sum += val
            else:
                left.add(val)
                left_sum += val
            balance()
            
        median = left[-1]
        cost[0] = median * (len(left) - len(right)) - left_sum + right_sum
        
        # Slide the window across the array
        for i in range(1, n - x + 1):
            # Remove the element leaving the window
            rem_val = nums[i - 1]
            if rem_val in left:
                left.remove(rem_val)
                left_sum -= rem_val
            else:
                right.remove(rem_val)
                right_sum -= rem_val
                
            # Add the new element entering the window
            add_val = nums[i + x - 1]
            if right and add_val >= right[0]:
                right.add(add_val)
                right_sum += add_val
            else:
                left.add(add_val)
                left_sum += add_val
                
            balance()
            
            median = left[-1]
            cost[i] = median * (len(left) - len(right)) - left_sum + right_sum

        # DP to find the minimum cost for k non-overlapping subarrays
        dp = [0] * (n + 1)
        
        for subarray_count in range(1, k + 1):
            next_dp = [float('inf')] * (n + 1)
            min_val = float('inf')
            
            for i in range(subarray_count * x, n + 1):
                # Transition from the best choice at i - x
                val = dp[i - x] + cost[i - x]
                if val < min_val:
                    min_val = val
                next_dp[i] = min_val
                
            dp = next_dp
            
        return dp[n]
