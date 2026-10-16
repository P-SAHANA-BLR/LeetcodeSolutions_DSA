class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.sum_val = [0] * (4 * n)
        self.sum_sq = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push(self, node, start, end):
        if self.lazy[node] == 0:
            return
        
        lazy_val = self.lazy[node]
        mid = (start + end) // 2
        
        # Left child
        self._apply(2 * node, start, mid, lazy_val)
        # Right child
        self._apply(2 * node + 1, mid + 1, end, lazy_val)
        
        self.lazy[node] = 0

    def _apply(self, node, start, end, val):
        num_elements = end - start + 1
        
        # New sum_sq = sum_sq + 2 * val * sum_val + val^2 * num_elements
        self.sum_sq[node] = (self.sum_sq[node] + 
                             2 * val * self.sum_val[node] + 
                             val * val * num_elements) % self.MOD
        
        # New sum_val = sum_val + val * num_elements
        self.sum_val[node] = (self.sum_val[node] + val * num_elements) % self.MOD
        
        self.lazy[node] = (self.lazy[node] + val) % self.MOD

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            self._apply(node, start, end, val)
            return
        
        self._push(node, start, end)
        mid = (start + end) // 2
        
        if l <= mid:
            self.update(2 * node, start, mid, l, r, val)
        if r > mid:
            self.update(2 * node + 1, mid + 1, end, l, r, val)
            
        self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % self.MOD
        self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % self.MOD


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        tree = SegmentTree(n)
        last_seen = {}
        total_ans = 0
        MOD = 10**9 + 7
        
        for j in range(n):
            # Find the previous occurrence of nums[j]
            last_idx = last_seen.get(nums[j], -1)
            
            # Increment distinct counts for all subarrays starting from last_idx + 1 to j
            tree.update(1, 0, n - 1, last_idx + 1, j, 1)
            
            # Add the sum of squares of all valid subarrays ending at j
            total_ans = (total_ans + tree.sum_sq[1]) % MOD
            
            # Update the last seen position of the element
            last_seen[nums[j]] = j
            
        return total_ans
