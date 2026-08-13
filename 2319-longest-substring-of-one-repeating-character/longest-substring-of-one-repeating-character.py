from typing import List

class SegmentTreeNode:
    __slots__ = ['max_len', 'pref_len', 'suff_len', 'size', 'left_char', 'right_char']
    def __init__(self, char: str = ''):
        # Initialize a leaf node representing a single character
        self.max_len = 1 if char else 0
        self.pref_len = 1 if char else 0
        self.suff_len = 1 if char else 0
        self.size = 1 if char else 0
        self.left_char = char
        self.right_char = char

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        # Using a 1D array of nodes for cache locality and speed
        tree = [None] * (4 * n)
        s_list = list(s)
        
        def merge(left: SegmentTreeNode, right: SegmentTreeNode) -> SegmentTreeNode:
            parent = SegmentTreeNode()
            parent.size = left.size + right.size
            parent.left_char = left.left_char
            parent.right_char = right.right_char
            
            # Initial boundaries take inner child values
            parent.pref_len = left.pref_len
            parent.suff_len = right.suff_len
            parent.max_len = max(left.max_len, right.max_len)
            
            # If the boundary characters match, bridge them
            if left.right_char == right.left_char:
                combined_mid = left.suff_len + right.pref_len
                if parent.max_len < combined_mid:
                    parent.max_len = combined_mid
                
                # Extend prefix if the entire left side matches the start of the right side
                if left.pref_len == left.size:
                    parent.pref_len = left.size + right.pref_len
                
                # Extend suffix if the entire right side matches the end of the left side
                if right.suff_len == right.size:
                    parent.suff_len = right.size + left.suff_len
                    
            return parent

        def build(node: int, start: int, end: int):
            if start == end:
                tree[node] = SegmentTreeNode(s_list[start])
                return
            mid = (start + end) // 2
            left_node = 2 * node
            right_node = 2 * node + 1
            build(left_node, start, mid)
            build(right_node, mid + 1, end)
            tree[node] = merge(tree[left_node], tree[right_node])

        def update(node: int, start: int, end: int, idx: int, char: str):
            if start == end:
                tree[node] = SegmentTreeNode(char)
                return
            mid = (start + end) // 2
            left_node = 2 * node
            right_node = 2 * node + 1
            if start <= idx <= mid:
                update(left_node, start, mid, idx, char)
            else:
                update(right_node, mid + 1, end, idx, char)
            tree[node] = merge(tree[left_node], tree[right_node])

        # Step 1: Construct the initial segment tree
        build(1, 0, n - 1)
        
        # Step 2: Execute queries and store maximum lengths
        ans = []
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            char = queryCharacters[i]
            
            # Only update if the character actually changes to save processing time
            if s_list[idx] != char:
                s_list[idx] = char
                update(1, 0, n - 1, idx, char)
                
            ans.append(tree[1].max_len)
            
        return ans
