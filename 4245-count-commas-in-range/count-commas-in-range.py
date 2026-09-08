class Solution:
    def countCommas(self, n: int) -> int:
        # Since n <= 10^5, every number from 1,000 to 100,000 
        # contains exactly 1 comma.
        if n < 1000:
            return 0
        
        return n - 1000 + 1