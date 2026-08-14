# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            # Base case: if boundaries cross, there are no elements to pick
            if left > right:
                return None
            
            # Pick the middle element to keep the tree balanced
            mid = (left + right) // 2
            
            # Create the root node with the middle element
            root = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        # Initialize the helper function with the full array boundaries
        return helper(0, len(nums) - 1)
