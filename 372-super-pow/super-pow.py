class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337
        # Handle cases where base 'a' is larger than 1337
        a %= MOD
        
        result = 1
        for digit in b:
            # result^10 * a^digit % MOD
            result = (pow(result, 10, MOD) * pow(a, digit, MOD)) % MOD
            
        return result
