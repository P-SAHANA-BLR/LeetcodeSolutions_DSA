import sys

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Binary lifting constants (2^16 = 65536 > 50000)
        LOG = 16  
        up = [[0] * LOG for _ in range(n)]
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        
        # Iterative DFS to avoid Python recursion limit issues
        timer = 0
        stack = [(0, 0, 0, 0)]  # (node, parent, depth, state) where state 0 = enter, 1 = exit
        
        # First pass to compute depth and binary lifting parents
        while stack:
            u, p, d, state = stack.pop()
            if state == 0:
                depth[u] = d
                up[u][0] = p
                for i in range(1, LOG):
                    up[u][i] = up[up[u][i-1]][i-1]
                
                timer += 1
                tin[u] = timer
                
                # Push exit state first
                stack.append((u, p, d, 1))
                # Push children
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u, d + 1, 0))
            else:
                tout[u] = timer

        # Function to find LCA using binary lifting
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            # Bring both nodes to the same depth
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            
            if u == v:
                return u
                
            # Lift both nodes simultaneously
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]
        
        # Fenwick Tree (Binary Indexed Tree) for range XOR updates
        bit = [0] * (timer + 2)
        
        def bit_update(idx, val):
            while idx <= timer:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def bit_query(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
        
        def update_subtree(u, char_mask):
            bit_update(tin[u], char_mask)
            bit_update(tout[u] + 1, char_mask)

        # Initialize the Fenwick tree with the initial node characters
        current_chars = list(s)
        for i in range(n):
            mask = 1 << (ord(current_chars[i]) - 97)
            update_subtree(i, mask)
            
        ans = []
        
        # Process queries
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                
                # Toggle old character out and new character in
                old_mask = 1 << (ord(current_chars[u]) - 97)
                new_mask = 1 << (ord(c) - 97)
                
                update_subtree(u, old_mask ^ new_mask)
                current_chars[u] = c
                
            else:  # query u v
                u = int(parts[1])
                v = int(parts[2])
                
                lca = get_lca(u, v)
                
                # Fetch root-to-node path masks
                mask_u = bit_query(tin[u])
                mask_v = bit_query(tin[v])
                
                # XOR cancels out the common root-to-LCA ancestor path
                path_mask = mask_u ^ mask_v
                
                # Manually add back the single character at the LCA node
                lca_char_mask = 1 << (ord(current_chars[lca]) - 97)
                path_mask ^= lca_char_mask
                
                # Check if at most one bit is set (meaning at most one odd-count character)
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans
