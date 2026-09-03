# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        # Map values to their indices in the inorder array for O(1) lookups
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Start from the last element of postorder (the root of the tree)
        self.post_idx = len(postorder) - 1
        
        def helper(in_start: int, in_end: int) -> Optional[TreeNode]:
            # Base case: if there are no elements to construct the sub-tree
            if in_start > in_end:
                return None
            
            # Current root value from postorder traversal
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            
            # Find the index of the root in inorder to split into left and right subtrees
            mid = inorder_idx_map[root_val]
            
            # Build right subtree first because we are traversing postorder backwards (Root -> Right -> Left)
            root.right = helper(mid + 1, in_end)
            root.left = helper(in_start, mid - 1)
            
            return root
            
        return helper(0, len(inorder) - 1)
