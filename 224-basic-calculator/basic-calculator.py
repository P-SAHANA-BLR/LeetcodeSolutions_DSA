class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        total = 0
        sign = 1  # 1 for '+', -1 for '-'
        
        i = 0
        n = len(s)
        
        # Track the last non-space character to identify unary minus
        last_char = '(' 
        
        while i < n:
            char = s[i]
            
            if char.isdigit():
                # Build the complete multi-digit integer
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                
                # Update the running total with the completed number
                total += sign * num
                # Decrement i because the outer loop will increment it
                i -= 1 
                last_char = 'd' # Mark that the last token processed was a digit
                
            elif char == '+':
                sign = 1
                last_char = '+'
                
            elif char == '-':
                # If '-' is at the start or follows an open parenthesis, it is unary
                if last_char == '(':
                    # We can simulate this by treating it as 0 - num
                    sign = -1
                else:
                    sign = -1
                last_char = '-'
                
            elif char == '(':
                # Push the current running total and sign onto the stack
                stack.append(total)
                stack.append(sign)
                
                # Reset total and sign for the inner expression context
                total = 0
                sign = 1
                last_char = '('
                
            elif char == ')':
                # Evaluate the expression inside the parenthesis
                prev_sign = stack.pop()
                prev_total = stack.pop()
                
                # Combine the inner expression result with the outer context
                total = prev_total + (prev_sign * total)
                last_char = ')'
                
            i += 1
            
        return total
