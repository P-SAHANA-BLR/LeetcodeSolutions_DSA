from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        # Initialize a queue and push the left and right children
        queue = deque([root.left, root.right])
        
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            
            # If both are null, continue checking the remaining elements
            if not t1 and not t2:
                continue
            # If only one is null, or values conflict, it's not symmetric
            if not t1 or not t2 or t1.val != t2.val:
                return False
                
            # Push children in mirrored order
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
            
        return True
