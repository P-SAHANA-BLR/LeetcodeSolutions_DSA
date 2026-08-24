class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Calculate prefix sums
        pref = [0] * n
        pref[0] = stones[0]
        for i in range(1, n):
            pref[i] = pref[i-1] + stones[i]
            
        # Base case: The only valid choice for the last remaining element 
        # is taking all stones up to the end (index n-1).
        dp = pref[-1]
        
        # Iterate backwards from index n-2 down to 1
        # Index 0 is not allowed because x must be > 1 (we must take at least 2 stones)
        for i in range(n - 2, 0, -1):
            dp = max(dp, pref[i] - dp)
            
        return dp
