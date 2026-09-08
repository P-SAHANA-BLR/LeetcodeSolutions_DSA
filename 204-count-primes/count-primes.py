class Solution:
    def countPrimes(self, n: int) -> int:
        # Base case: there are no primes strictly less than 2
        if n <= 2:
            return 0
        
        # Initialize a boolean array tracking primality status
        # Index represents the number, value represents if it's prime
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        
        # Sieve up to the square root of n
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i starting from i*i as composite
                # Step size is i because every i-th number is a multiple
                is_prime[i*i : n : i] = [False] * len(is_prime[i*i : n : i])
                
        # Count the number of True values remaining in the array
        return sum(is_prime)
