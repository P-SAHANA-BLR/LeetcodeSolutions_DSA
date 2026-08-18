from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse the array backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 and carries over
            digits[i] = 0
            
        # If all digits were 9, we need an extra 1 at the front
        return [1] + digits
