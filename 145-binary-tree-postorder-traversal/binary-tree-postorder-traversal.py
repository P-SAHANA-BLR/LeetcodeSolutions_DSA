class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node):
            if not node:
                return
            traverse(node.left)    # Visit Left
            traverse(node.right)   # Visit Right
            result.append(node.val) # Visit Root
            
        traverse(root)
        return result
