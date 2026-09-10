# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.matching_nodes = 0
        
        def traverse(node):
            if not node:
                return 0, 0  # (sum, count)
            
            # Get the sum and count from the left and right subtrees
            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)
            
            # Calculate total sum and total count for the current subtree
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Check if the node value equals the integer division average
            if node.val == current_sum // current_count:
                self.matching_nodes += 1
                
            return current_sum, current_count

        traverse(root)
        return self.matching_nodes
