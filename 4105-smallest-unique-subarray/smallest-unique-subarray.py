from collections import Counter
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Quick check for length 1
        counts = Counter(nums)
        if 1 in counts.values():
            return 1
            
        # Double hashing constants to avoid collisions
        BASE1, MOD1 = 1315423911, 10**9 + 7
        BASE2, MOD2 = 2654435761, 10**9 + 9
        
        # Precompute powers for rolling hash
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * BASE1) % MOD1
            pow2[i] = (pow2[i - 1] * BASE2) % MOD2
            
        def has_unique_subarray(length: int) -> bool:
            h1, h2 = 0, 0
            # Compute hash for the first window of size `length`
            for i in range(length):
                h1 = (h1 * BASE1 + nums[i]) % MOD1
                h2 = (h2 * BASE2 + nums[i]) % MOD2
                
            freq = Counter()
            freq[(h1, h2)] += 1
            
            # Slide the window across the array
            for i in range(length, n):
                out_val = nums[i - length]
                in_val = nums[i]
                
                h1 = ((h1 - out_val * pow1[length - 1]) * BASE1 + in_val) % MOD1
                h2 = ((h2 - out_val * pow2[length - 1]) * BASE2 + in_val) % MOD2
                
                freq[(h1, h2)] += 1
                
            return 1 in freq.values()

        # Binary search for the minimum valid length
        low, high = 2, n
        ans = n
        
        while low <= high:
            mid = (low + high) // 2
            if has_unique_subarray(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
