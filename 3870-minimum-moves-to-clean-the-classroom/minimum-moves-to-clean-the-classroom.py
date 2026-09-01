from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        
        start_r, start_c = -1, -1
        litter_positions = []
        
        # Parse the grid to locate 'S' and all 'L' cells
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_positions.append((r, c))
        
        num_litter = len(litter_positions)
        # Map each litter's coordinate to its unique bit index
        litter_map = {pos: i for i, pos in enumerate(litter_positions)}
        
        # Target mask representing all litter collected
        target_mask = (1 << num_litter) - 1
        
        # Handle the edge case where there is no litter to collect initially
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
            
        # Visited set stores: (row, col, remaining_energy, litter_mask)
        visited = set()
        visited.add((start_r, start_c, energy, initial_mask))
        
        # Queue stores: (row, col, current_energy, litter_mask, moves)
        queue = deque([(start_r, start_c, energy, initial_mask, 0)])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, curr_energy, mask, moves = queue.popleft()
            
            # If all litter is collected, return the total moves
            if mask == target_mask:
                return moves
            
            # If out of energy, we cannot move further from this state
            if curr_energy == 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries and obstacles
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = curr_energy - 1
                    next_mask = mask
                    
                    # Update mask if the next cell contains uncollected litter
                    if classroom[nr][nc] == 'L' and (nr, nc) in litter_map:
                        next_mask |= (1 << litter_map[(nr, nc)])
                    
                    # Reset energy if the next cell is a reset station
                    if classroom[nr][nc] == 'R':
                        next_energy = energy
                        
                    # Enqueue the new state if it hasn't been visited before
                    state = (nr, nc, next_energy, next_mask)
                    if state not in visited:
                        visited.add(state)
                        queue.append((nr, nc, next_energy, next_mask, moves + 1))
                        
        return -1
