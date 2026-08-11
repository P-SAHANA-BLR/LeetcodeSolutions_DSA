class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp1, dp2, dp3 = 0, 0, 0
        for i in range(n - 1, -1, -1):
            take1 = stoneValue[i] - dp1
            take2 = stoneValue[i] + stoneValue[i + 1] - dp2 if i + 1 < n else float('-inf')
            take3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp3 if i + 2 < n else float('-inf')
            current_dp = max(take1, take2, take3)
            dp3 = dp2
            dp2 = dp1
            dp1 = current_dp
        if dp1 > 0:
            return "Alice"
        elif dp1 < 0:
            return "Bob"
        else:
            return "Tie"
