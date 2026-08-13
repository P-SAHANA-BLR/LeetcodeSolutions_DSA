from typing import List

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        nums = [ord(c) - ord('a') for c in s]
        n = len(s)
        
        base = 26
        mod1 = 10**9 + 7
        # FIX: Changed 2^31 - 1 to 2**31 - 1
        mod2 = 2**31 - 1 
        
        def check(length: int) -> int:
            if length == 0:
                return 0
                
            h1_multiplier = pow(base, length, mod1)
            h2_multiplier = pow(base, length, mod2)
            
            h1 = 0
            h2 = 0
            for i in range(length):
                h1 = (h1 * base + nums[i]) % mod1
                h2 = (h2 * base + nums[i]) % mod2
                
            seen = {(h1, h2)}
            
            for start in range(1, n - length + 1):
                h1 = (h1 * base - nums[start - 1] * h1_multiplier + nums[start + length - 1]) % mod1
                h2 = (h2 * base - nums[start - 1] * h2_multiplier + nums[start + length - 1]) % mod2
                
                if h1 < 0: h1 += mod1
                if h2 < 0: h2 += mod2
                
                current_hash_pair = (h1, h2)
                if current_hash_pair in seen:
                    return start
                seen.add(current_hash_pair)
                
            return -1

        low = 1
        high = n - 1
        start_idx = -1
        best_len = 0
        
        while low <= high:
            mid = (low + high) // 2
            possible_start = check(mid)
            
            if possible_start != -1:
                start_idx = possible_start
                best_len = mid
                low = mid + 1  
            else:
                high = mid - 1 
                
        return s[start_idx : start_idx + best_len] if start_idx != -1 else ""
