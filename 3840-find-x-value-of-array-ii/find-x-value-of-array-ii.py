from typing import List

class SegmentTree:
    def __init__(self, n: int, k: int):
        self.n = n
        self.k = k
        # Each node stores: [product_mod_k, [count_for_rem_0, ..., count_for_rem_k-1]]
        self.tree = [[1, [0] * k] for _ in range(4 * n)]
        
    def _merge(self, left, right):
        left_prod, left_dp = left
        right_prod, right_dp = right
        
        merged_prod = (left_prod * right_prod) % self.k
        merged_dp = list(left_dp)
        
        for r_rem, count in enumerate(right_dp):
            if count > 0:
                new_rem = (r_rem * left_prod) % self.k
                merged_dp[new_rem] += count
                
        return [merged_prod, merged_dp]

    def build(self, arr, node, start, end):
        if start == end:
            val = arr[start] % self.k
            dp = [0] * self.k
            dp[val] = 1
            self.tree[node] = [val, dp]
            return
            
        mid = (start + end) // 2
        self.build(arr, 2 * node, start, mid)
        self.build(arr, 2 * node + 1, mid + 1, end)
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, node, start, end, idx, val):
        if start == end:
            v = val % self.k
            dp = [0] * self.k
            dp[v] = 1
            self.tree[node] = [v, dp]
            return
            
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        # Returns [product, dp_array] for the range [l, r]
        if l <= start and end <= r:
            return self.tree[node]
            
        mid = (start + end) // 2
        if r <= mid:
            return self.query(2 * node, start, mid, l, r)
        if l > mid:
            return self.query(2 * node + 1, mid + 1, end, l, r)
            
        left_res = self.query(2 * node, start, mid, l, mid)
        right_res = self.query(2 * node + 1, mid + 1, end, mid + 1, r)
        return self._merge(left_res, right_res)

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(n, k)
        st.build(nums, 1, 0, n - 1)
        
        ans = []
        for index, value, start, x in queries:
            st.update(1, 0, n - 1, index, value)
            # Query the suffix range from `start` to `n - 1`
            _, dp = st.query(1, 0, n - 1, start, n - 1)
            ans.append(dp[x])
            
        return ans
