class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Candidate amounts of type 3 items to buy
        # The mathematical minimum is guaranteed to be at one of these vertices
        ans = float('inf')
        
        for x in (0, need1, need2):
            # Cost = (x * costBoth) + remaining needed for type 1 + remaining needed for type 2
            rem1 = need1 - x if need1 > x else 0
            rem2 = need2 - x if need2 > x else 0
            
            cost = (x * costBoth) + (rem1 * cost1) + (rem2 * cost2)
            if cost < ans:
                ans = cost
                
        return ans
