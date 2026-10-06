class Solution:
    def totalNQueens(self, n: int) -> int:
        # Sets to track columns and diagonals currently under attack
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)
        
        self.solutions_count = 0
        
        def backtrack(r):
            # Base Case: If we successfully placed queens in all rows (0 to n-1)
            if r == n:
                self.solutions_count += 1
                return
            
            # Try placing a queen in each column of the current row 'r'
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue  # Under attack, skip this column
                
                # Place the queen and mark paths as attacked
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # Move to the next row
                backtrack(r + 1)
                
                # Backtrack: Remove the queen and clear the paths
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                
        backtrack(0)
        return self.solutions_count
