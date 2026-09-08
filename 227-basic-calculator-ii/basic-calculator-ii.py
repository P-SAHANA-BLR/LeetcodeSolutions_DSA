class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
            
        current_number = 0
        last_operator = '+'
        
        # Track values to avoid using a stack list
        total_sum = 0
        last_term = 0
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
                
            # Process the operator if we hit a non-space character 
            # OR if we reach the end of the string
            if char in "+-*/" or i == len(s) - 1:
                if last_operator == '+':
                    total_sum += last_term
                    last_term = current_number
                elif last_operator == '-':
                    total_sum += last_term
                    last_term = -current_number
                elif last_operator == '*':
                    last_term = last_term * current_number
                elif last_operator == '/':
                    # Python's // truncates toward negative infinity (e.g., -3 // 2 = -2)
                    # The problem requires truncation toward zero, so we use int() division
                    last_term = int(last_term / current_number)
                    
                # Update the operator and reset the current number digits
                last_operator = char
                current_number = 0
                
        # Add the very last evaluated block to the sum
        total_sum += last_term
        return total_sum
