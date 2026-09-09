import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of available numbers to build the permutation
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Convert k to 0-indexed
        k -= 1
        
        result = []
        
        # Calculate (n-1)! to determine block sizes
        factorial = math.factorial(n - 1)
        
        for i in range(n - 1, -1, -1):
            # Find the index of the current digit
            idx = k // factorial
            result.append(numbers.pop(idx))
            
            # Update k for the remaining positions
            k %= factorial
            
            # Reduce the factorial size for the next iteration if positions remain
            if i > 0:
                factorial //= i
                
        return "".join(result)
