# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_height(node: Optional[TreeNode]) -> int:
            # Base case: An empty tree has a height of 0 and is balanced
            if not node:
                return 0
            
            # Check the height of the left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced
            
            # Check the height of the right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced
            
            # If the current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            # Otherwise, return the height of the current node
            return 1 + max(left_height, right_height)
            
        # If check_height doesn't return -1, the tree is balanced
        return check_height(root) != -1
