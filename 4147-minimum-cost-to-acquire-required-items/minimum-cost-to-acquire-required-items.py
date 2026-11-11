class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # The optimal number of type 3 items will always be one of these three boundary points
        candidates = [0, need1, need2]
        
        min_total_cost = float('inf')
        
        for x in candidates:
            # Cost of buying x items of type 3 + remaining needed for type 1 + remaining needed for type 2
            current_cost = (x * costBoth) + (max(0, need1 - x) * cost1) + (max(0, need2 - x) * cost2)
            if current_cost < min_total_cost:
                min_total_cost = current_cost
                
        return min_total_cost
