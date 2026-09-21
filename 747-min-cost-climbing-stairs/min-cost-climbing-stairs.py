class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Track the minimum cost to reach the last two steps
        # down_one represents min cost to reach step i-1
        # down_two represents min cost to reach step i-2
        down_one = 0
        down_two = 0
        
        # Iterate from step 2 up to the top of the staircase (index n)
        for i in range(2, len(cost) + 1):
            # Calculate the cost to reach step i
            current = min(down_one + cost[i - 1], down_two + cost[i - 2])
            
            # Update pointers for the next iteration
            down_two = down_one
            down_one = current
            
        return down_one
