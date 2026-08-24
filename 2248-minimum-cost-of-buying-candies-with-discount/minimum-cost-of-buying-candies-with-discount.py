class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort costs in descending order
        cost.sort(reverse=True)
        
        total_cost = 0
        
        # Iterate through the array
        for i in range(len(cost)):
            # Skip every 3rd candy (index 2, 5, 8, ...) as it is free
            if (i + 1) % 3 == 0:
                continue
            total_cost += cost[i]
            
        return total_cost
