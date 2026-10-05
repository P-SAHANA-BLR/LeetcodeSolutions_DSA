class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # The stack stores the scores of the current inner contexts.
        # We start with a base score of 0 for the outermost layer.
        stack = [0]
        
        for char in s:
            if char == '(':
                # Entering a new nested layer, start its score at 0
                stack.append(0)
            else:
                # Exiting a layer. Pop the score of the inner layer.
                inner_score = stack.pop()
                
                # Rule 1 & 3: "()" gives 1, "(A)" gives 2 * A
                current_score = max(2 * inner_score, 1)
                
                # Rule 2: AB gives A + B. 
                # Add the computed score to the parent layer's total.
                stack[-1] += current_score
                
        return stack[0]
