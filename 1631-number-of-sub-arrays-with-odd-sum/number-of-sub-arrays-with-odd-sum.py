class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        # Start with even_count = 1 to represent the empty prefix sum (0 is even)
        even_count = 1
        odd_count = 0
        
        prefix_sum = 0
        result = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 1:
                # Current prefix sum is odd; pair with all previous even prefix sums
                result = (result + even_count) % MOD
                odd_count += 1
            else:
                # Current prefix sum is even; pair with all previous odd prefix sums
                result = (result + odd_count) % MOD
                even_count += 1
                
        return result
