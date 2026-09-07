class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
            
        # Divide by 2 as much as possible
        while n % 2 == 0:
            n //= 2
            
        # Divide by 3 as much as possible
        while n % 3 == 0:
            n //= 3
            
        # Divide by 5 as much as possible
        while n % 5 == 0:
            n //= 5
                
        # If n is reduced to 1, it is an ugly number
        return n == 1
