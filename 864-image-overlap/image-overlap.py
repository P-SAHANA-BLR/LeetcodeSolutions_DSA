from collections import defaultdict
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Extract coordinates of all 1s in both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Dictionary to store the frequency of each transformation vector
        shift_counts = defaultdict(int)
        max_overlap = 0
        
        # Calculate shifts between every pair of 1s
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift_vector = (r2 - r1, c2 - c1)
                shift_counts[shift_vector] += 1
                max_overlap = max(max_overlap, shift_counts[shift_vector])
                
        return max_overlap
