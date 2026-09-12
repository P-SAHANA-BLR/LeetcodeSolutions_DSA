from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Bitmasks to track used numbers in rows, columns, and 3x3 boxes
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        empty_cells = []
        
        # Initialize masks with pre-existing numbers and collect empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    val = int(board[r][c]) - 1
                    mask = 1 << val
                    box_idx = (r // 3) * 3 + (c // 3)
                    
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_idx] |= mask
                    
        def backtrack(cell_idx: int) -> bool:
            # If all empty cells are filled successfully, the puzzle is solved
            if cell_idx == len(empty_cells):
                return True
                
            r, c = empty_cells[cell_idx]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Combine masks to find which numbers are already taken in row, col, or box
            taken = rows[r] | cols[c] | boxes[box_idx]
            
            # Try placing digits 1-9 (represented by shifts 0-8)
            for val in range(9):
                mask = 1 << val
                # If the bit is not set, the digit is valid to place
                if not (taken & mask):
                    # Place the digit and update masks
                    board[r][c] = str(val + 1)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_idx] |= mask
                    
                    # Recursively proceed to the next empty cell
                    if backtrack(cell_idx + 1):
                        return True
                        
                    # Backtrack: remove the digit and clear the masks
                    rows[r] ^= mask
                    cols[c] ^= mask
                    boxes[box_idx] ^= mask
                    board[r][c] = '.'
                    
            return False

        backtrack(0)
