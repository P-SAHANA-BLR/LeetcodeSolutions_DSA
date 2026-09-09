class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Helper function to compute nCr % MOD
        def nCr(N, R):
            if R < 0 or R > N:
                return 0
            if R == 0 or R == N:
                return 1
            # Compute numerator and denominator
            num = 1
            den = 1
            # Optimize to choose smaller R
            if R > N - R:
                R = N - R
            for i in range(R):
                num = (num * (N - i)) % MOD
                den = (den * (i + 1)) % MOD
            # Multiply by modular inverse of denominator
            return (num * pow(den, MOD - 2, MOD)) % MOD
        
        # 1. Total sequences summing to n with k positive numbers
        total_sequences = nCr(n - 1, k - 1)
        
        # 2. Sequences where ALL numbers are odd
        all_odd_sequences = 0
        if (n - k) % 2 == 0:
            all_odd_sequences = nCr((n + k) // 2 - 1, k - 1)
            
        # 3. Answer is Total - All-Odd
        return (total_sequences - all_odd_sequences + MOD) % MOD
