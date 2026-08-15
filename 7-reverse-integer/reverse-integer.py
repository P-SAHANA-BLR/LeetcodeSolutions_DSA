class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer bounds
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        res = 0
        # Determine the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            # Extract the last digit
            pop = x % 10
            x //= 10
            
            # Check for overflow before multiplying by 10
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > INT_MAX % 10):
                return 0
                
            res = res * 10 + pop
            
        return sign * res
