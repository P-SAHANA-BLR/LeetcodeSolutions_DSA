class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Assign to group 0 if current depth is even, group 1 if odd
                ans.append(depth % 2)
                depth += 1
            else:
                # Decrement depth first since we are closing a parenthesis
                depth -= 1
                ans.append(depth % 2)
                
        return ans
