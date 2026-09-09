class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
            
        count = 0
        i = 1  # Start at the ones place
        
        while i <= n:
            higher = n // (i * 10)
            current = (n // i) % 10
            lower = n % i
            
            # Count contributions from full cycles of higher digits
            if current == 0:
                count += higher * i
            elif current == 1:
                count += higher * i + (lower + 1)
            else:
                count += (higher + 1) * i
                
            # Move to the next place value (tens, hundreds, etc.)
            i *= 10
            
        return count
