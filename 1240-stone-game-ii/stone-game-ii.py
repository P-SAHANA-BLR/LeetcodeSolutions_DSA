from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums to easily find total remaining stones
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @lru_cache(None)
        def dfs(i: int, M: int) -> int:
            # If the current player can take all remaining piles, take them all
            if i + 2 * M >= n:
                return suffix_sum[i]
                
            # Otherwise, find the option X that maximizes the current player's stones
            max_stones = 0
            for x in range(1, 2 * M + 1):
                # Total remaining stones minus what the opponent optimally takes
                current_choice_stones = suffix_sum[i] - dfs(i + x, max(M, x))
                max_stones = max(max_stones, current_choice_stones)
                
            return max_stones
            
        # starts at index 0 with M = 1
        return dfs(0, 1)
