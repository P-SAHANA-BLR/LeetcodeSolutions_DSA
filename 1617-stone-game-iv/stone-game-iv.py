class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] represents whether the player starting with i stones can win
        dp = [False] * (n + 1)
        
        # Base case: dp[0] is False because a player with 0 stones has no moves and loses.
        
        for i in range(1, n + 1):
            k = 1
            # Try removing every non-zero perfect square less than or equal to i
            while k * k <= i:
                if not dp[i - k * k]:
                    # If this move forces the opponent into a losing state, we win!
                    dp[i] = True
                    break  # Short-circuit early as one winning move is enough
                k += 1
                
        return dp[n]
