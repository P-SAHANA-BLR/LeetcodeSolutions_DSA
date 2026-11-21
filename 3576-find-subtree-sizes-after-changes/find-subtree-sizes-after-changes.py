import sys
from typing import List

# Increase recursion depth for deep trees up to 10^5 nodes
sys.setrecursionlimit(200000)


class Solution:

    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = list(parent)
        last_seen = [-1] * 26

        # Step 1: DFS on original tree to determine new parents
        def dfs_reparent(u: int) -> None:
            char_idx = ord(s[u]) - ord('a')
            prev_ancestor = last_seen[char_idx]

            if prev_ancestor != -1:
                new_parent[u] = prev_ancestor

            last_seen[char_idx] = u
            for v in adj[u]:
                dfs_reparent(v)
            last_seen[char_idx] = prev_ancestor

        dfs_reparent(0)

        # Step 2: Build the modified tree and compute subtree sizes
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        ans = [1] * n

        def dfs_size(u: int) -> int:
            for v in new_adj[u]:
                ans[u] += dfs_size(v)
            return ans[u]

        dfs_size(0)
        return ans
