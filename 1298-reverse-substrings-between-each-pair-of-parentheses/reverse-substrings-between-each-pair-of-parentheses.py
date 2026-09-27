class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        # pair[i] will store the index of the matching parenthesis for index i
        pair = [0] * n
        
        # Step 1: Pair up the matching parentheses using a stack
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        # Step 2: Traverse the string using the wormhole simulation
        result = []
        curr_idx = 0
        direction = 1 # 1 means moving right, -1 means moving left
        
        while curr_idx < n:
            if s[curr_idx] == '(' or s[curr_idx] == ')':
                # Teleport to the matching parenthesis
                curr_idx = pair[curr_idx]
                # Reverse the traversal direction
                direction = -direction
            else:
                # Append normal characters to the result
                result.append(s[curr_idx])
            
            # Step forward in the current direction
            curr_idx += direction
            
        return "".join(result)
