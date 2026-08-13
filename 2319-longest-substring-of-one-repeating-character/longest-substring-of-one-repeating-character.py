from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        
        # 1. Expand size to the next power of 2 for a perfectly balanced iterative tree
        size = 1
        while size < n:
            size *= 2
            
        # 2. Pre-allocate parallel flat arrays to avoid object overhead
        max_len = [0] * (2 * size)
        pref_len = [0] * (2 * size)
        suff_len = [0] * (2 * size)
        left_char = [''] * (2 * size)
        right_char = [''] * (2 * size)
        node_size = [0] * (2 * size)
        
        # 3. Initialize leaf nodes at the base level (indices size to size + n - 1)
        for i in range(n):
            idx = size + i
            max_len[idx] = 1
            pref_len[idx] = 1
            suff_len[idx] = 1
            left_char[idx] = s[i]
            right_char[idx] = s[i]
            node_size[idx] = 1
            
        # Initialize remaining dummy nodes to avoid boundary issues
        for i in range(n, size):
            node_size[size + i] = 1
            
        # 4. Iterative tree building function (bottom-up merge logic)
        def pull(i: int):
            left = 2 * i
            right = 2 * i + 1
            
            node_size[i] = node_size[left] + node_size[right]
            left_char[i] = left_char[left]
            right_char[i] = right_char[right]
            
            m_len = max(max_len[left], max_len[right])
            p_len = pref_len[left]
            s_len = suff_len[right]
            
            # Bridge boundary strings if adjacent characters match
            if right_char[left] == left_char[right]:
                mid = suff_len[left] + pref_len[right]
                if mid > m_len: 
                    m_len = mid
                if pref_len[left] == node_size[left]:
                    p_len = node_size[left] + pref_len[right]
                if suff_len[right] == node_size[right]:
                    s_len = node_size[right] + suff_len[left]
                    
            max_len[i] = m_len
            pref_len[i] = p_len
            suff_len[i] = s_len

        # Fill the segment tree from base to root
        for i in range(size - 1, 0, -1):
            pull(i)
            
        # 5. Process queries iteratively
        ans = []
        for q_char, q_idx in zip(queryCharacters, queryIndices):
            idx = size + q_idx
            
            # Fast-forward path: Skip update if character did not change
            if left_char[idx] != q_char:
                left_char[idx] = q_char
                right_char[idx] = q_char
                
                # Move up the tree iteratively to update affected parents
                idx //= 2
                while idx > 0:
                    pull(idx)
                    idx //= 2
                    
            ans.append(max_len[1])
            
        return ans
