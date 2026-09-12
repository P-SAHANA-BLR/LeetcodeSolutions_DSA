from typing import List
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Augment each interval with its original index: (left, right, weight, original_index)
        A = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        
        # Sort intervals by their start time
        A.sort(key=lambda x: x[0])
        
        n = len(A)
        starts = [x[0] for x in A]
        
        # Precompute the next non-overlapping interval index for each interval
        next_idx = []
        for i in range(n):
            # Find the first interval whose start time is > current interval's end time
            idx = bisect_left(starts, A[i][1] + 1)
            next_idx.append(idx)
            
        # dp[i][j] stores a tuple: (maximum_weight, sorted_indices_list)
        # Suffix DP: processing from right to left
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        # Helper function to determine if path 1 is better than path 2
        def is_better(w1, ind1, w2, ind2):
            if w1 != w2:
                return w1 > w2
            return ind1 < ind2

        for i in range(n - 1, -1, -1):
            for j in range(1, 5):
                # Option 1: Skip the current interval
                skip_w, skip_ind = dp[i + 1][j]
                
                # Option 2: Take the current interval
                nxt = next_idx[i]
                take_next_w, take_next_ind = dp[nxt][j - 1]
                take_w = A[i][2] + take_next_w
                take_ind = sorted(take_next_ind + [A[i][3]])
                
                # Choose the path that maximizes weight, breaking ties lexicographically
                if is_better(take_w, take_ind, skip_w, skip_ind):
                    dp[i][j] = (take_w, take_ind)
                else:
                    dp[i][j] = (skip_w, skip_ind)
                    
        # Return the best combination of indices using all intervals with up to 4 choices
        return dp[0][4][1]
