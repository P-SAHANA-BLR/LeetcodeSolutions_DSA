from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Group reserved seats by row using bitmasks
        # We only need to track seats 2 through 9
        rows = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] |= (1 << (seat - 2))
        
        # Bitmasks for the three valid 4-seat blocks
        # 15  is binary 00001111 (seats 2, 3, 4, 5)
        # 240 is binary 11110000 (seats 6, 7, 8, 9)
        # 60  is binary 00111100 (seats 4, 5, 6, 7)
        left_mask = 15
        right_mask = 240
        middle_mask = 60
        
        # Start by assuming all rows with reservations accommodate 0 families initially
        # Rows with NO reservations automatically get 2 families each
        max_groups = (n - len(rows)) * 2
        
        for mask in rows.values():
            families_in_row = 0
            left_free = (mask & left_mask) == 0
            right_free = (mask & right_mask) == 0
            
            if left_free:
                families_in_row += 1
            if right_free:
                families_in_row += 1
                
            # If neither the left nor right side fits a full family on its own,
            # check if the middle block is entirely open.
            if not left_free and not right_free:
                if (mask & middle_mask) == 0:
                    families_in_row += 1
                    
            max_groups += families_in_row
            
        return max_groups
