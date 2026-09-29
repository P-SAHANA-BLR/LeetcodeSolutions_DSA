class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
        
        # If the start is ')' or the end is '(', it can never be valid
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
            
        memo = {}
        
        def dfs(r, c, bal):
            # Update balance based on the current cell's character
            bal += 1 if grid[r][c] == '(' else -1
            
            # If balance goes negative, this path is invalid
            if bal < 0:
                return False
                
            # If we reached the bottom-right corner, check if balance is perfectly 0
            if r == m - 1 and c == n - 1:
                return bal == 0
                
            state = (r, c, bal)
            if state in memo:
                return memo[state]
                
            # Explore moving down or moving right
            res = False
            if r + 1 < m:
                res = res or dfs(r + 1, c, bal)
            if c + 1 < n:
                res = res or dfs(r, c + 1, bal)
                
            memo[state] = res
            return res
            
        return dfs(0, 0, 0)
