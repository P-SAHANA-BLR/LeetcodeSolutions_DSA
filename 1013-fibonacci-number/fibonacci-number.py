class Solution:
    def fib(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        a, b = 0, 1
        # Compute iteratively from 2 up to n
        for _ in range(2, n + 1):
            a, b = b, a + b
            
        return b
