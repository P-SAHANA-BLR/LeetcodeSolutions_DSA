class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Step 1: Count frequencies of remainders modulo 3
        cnt = [0, 0, 0]
        for stone in stones:
            cnt[stone % 3] += 1
            
        # Step 2: Separate counts for clarity
        c0, c1, c2 = cnt[0], cnt[1], cnt[2]
        
        # Step 3: Apply Game Theory based on the parity of zero-remainder stones
        if c0 % 2 == 0:
            # If count of 0s is even, Alice wins if both 1s and 2s exist
            return min(c1, c2) > 0
        else:
            # If count of 0s is odd, Alice wins if one remainder group heavily dominates the other
            return abs(c1 - c2) > 2
