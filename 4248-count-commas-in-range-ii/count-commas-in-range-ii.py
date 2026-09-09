class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        # The first comma appears at 1,000 (10^3)
        # The constraints go up to 10^15, so we check thresholds up to 10^15
        threshold = 1000
        
        while n >= threshold:
            # Number of integers from threshold to n inclusive
            total_commas += (n - threshold + 1)
            # Move to the next comma threshold (millions, billions, etc.)
            threshold *= 1000
            
        return total_commas
