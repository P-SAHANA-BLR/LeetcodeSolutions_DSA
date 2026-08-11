class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        
        # Loop through the prices starting from the second day
        for i in range(1, len(prices)):
            # If the price increased compared to the previous day, lock in the profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit
