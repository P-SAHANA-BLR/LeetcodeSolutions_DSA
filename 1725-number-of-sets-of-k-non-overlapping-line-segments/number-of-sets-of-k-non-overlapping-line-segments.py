import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # Total pool of points after accounting for shared endpoints
        total_points = n + k - 1
        # We need to choose exactly 2k endpoints for the k segments
        choose_endpoints = 2 * k
        
        # Modulo constant as requested
        MOD = 10**9 + 7
        
        # Calculate combination and take modulo
        return math.comb(total_points, choose_endpoints) % MOD
