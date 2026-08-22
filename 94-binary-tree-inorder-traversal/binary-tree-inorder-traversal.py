# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        
        while curr or stack:
            # Reach the leftmost node of the current node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Current must be NULL at this point
            curr = stack.pop()
            result.append(curr.val) # Add the root value
            
            # We have visited the node and its left subtree. 
            # Now, it's the right subtree's turn.
            curr = curr.right
            
        return result
