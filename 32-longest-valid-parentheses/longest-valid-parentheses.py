class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Base boundary index to handle valid strings starting at index 0
        stack = [-1]
        max_len = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                # Push the index of the open parenthesis
                stack.append(i)
            else:
                # Pop the most recent unmatched opening parenthesis index
                stack.pop()
                
                if not stack:
                    # If empty, the current ')' is unmatched and becomes the new boundary base
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
