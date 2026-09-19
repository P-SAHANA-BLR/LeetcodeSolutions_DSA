from collections import Counter

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        # --- Pruning 1: Quick Character Frequency Check ---
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
                
        # --- Pruning 2: Reverse Word to Optimise Starting Branching ---
        # Start from the end if the last character is rarer than the first character
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
            
        def dfs(r, c, index):
            # Base Case: Found the whole word
            if index == len(word):
                return True
                
            # Out of bounds or character mismatch
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[index]:
                return False
                
            # Temporarily mark the cell as visited to prevent reuse
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore all 4 adjacent directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
                     
            # Backtrack: Restore the original character
            board[r][c] = temp
            
            return found

        # Launch DFS from each cell matching the first letter
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
                        
        return False
