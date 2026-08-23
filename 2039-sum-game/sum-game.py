class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        # Calculate sums and question mark counts for both halves
        sum_L = sum(int(c) for c in num[:mid] if c != '?')
        sum_R = sum(int(c) for c in num[mid:] if c != '?')
        
        q_L = num[:mid].count('?')
        q_R = num[mid:].count('?')
        
        # If the total number of '?' is odd, Alice always wins
        if (q_L + q_R) % 2 != 0:
            return True
            
        # For Bob to win, the difference in sums must be perfectly balanced 
        # by the difference in '?' counts (each pair of '?' contributes 9 points)
        return (sum_L - sum_R) != (q_R - q_L) // 2 * 9
