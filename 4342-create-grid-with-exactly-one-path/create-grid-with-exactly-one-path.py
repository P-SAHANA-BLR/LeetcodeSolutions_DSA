class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Handle the edge case where there's only 1 column
        if n == 1:
            return ["."] * m
            
        # Initialize the entire grid with obstacles '#'
        grid = [["#"] * n for _ in range(m)]
        
        # 1. Open the first row up to column n - 2
        for j in range(n - 1):
            grid[0][j] = "."
            
        # 2. Open the column n - 2 from row 0 down to row m - 1
        for i in range(m):
            grid[i][n - 2] = "."
            
        # 3. Open the last row from column n - 2 to column n - 1
        grid[m - 1][n - 1] = "."
        
        # Convert each row from a list of characters to a string
        return ["".join(row) for row in grid]
