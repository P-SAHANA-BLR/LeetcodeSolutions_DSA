from typing import List
from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # Step 1: Count the availability of each digit in the input
        available_counts = Counter(digits)
        valid_count = 0
        
        # Step 2: Iterate through all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            # Extract digits
            d1 = num // 100          # Hundreds place
            d2 = (num // 10) % 10    # Tens place
            d3 = num % 10            # Units place
            
            # Count the frequency of digits needed for the current number
            needed_counts = Counter([d1, d2, d3])
            
            # Step 3: Verify if we have enough available digits
            possible = True
            for digit, count in needed_counts.items():
                if available_counts[digit] < count:
                    possible = False
                    break
            
            # Step 4: If valid, increment our counter
            if possible:
                valid_count += 1
                
        return valid_count
