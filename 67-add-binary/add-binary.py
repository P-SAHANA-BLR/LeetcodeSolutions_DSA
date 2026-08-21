class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        
        # Pointers starting at the end of both strings
        i = len(a) - 1
        j = len(b) - 1
        
        # Process strings from right to left
        while i >= 0 or j >= 0 or carry:
            total_sum = carry
            
            if i >= 0:
                total_sum += int(a[i])
                i -= 1
                
            if j >= 0:
                total_sum += int(b[j])
                j -= 1
                
            # Extract the bit (0 or 1)
            current_digit = str(total_sum % 2)
            
            # Concatenate to the front to avoid reversing later
            result = current_digit + result
            
            # Update the carry
            carry = total_sum // 2
            
        return result
