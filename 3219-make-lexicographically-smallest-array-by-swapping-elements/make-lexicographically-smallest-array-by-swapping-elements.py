from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        # Pair each number with its original index and sort by value
        sorted_pairs = sorted([(nums[i], i) for i in range(n)], key=lambda x: x[0])
        
        # This will hold our final answer array
        result = [0] * n
        
        # Group together elements that can reach each other via chains
        i = 0
        while i < n:
            j = i + 1
            # Expand the group as long as adjacent sorted elements are within the limit
            while j < n and sorted_pairs[j][0] - sorted_pairs[j-1][0] <= limit:
                j += 1
            
            # Extract elements and their corresponding indices for the current group
            group_elements = [sorted_pairs[k][0] for k in range(i, j)]
            group_indices = sorted([sorted_pairs[k][1] for k in range(i, j)])
            
            # Place sorted elements back into sorted indices to minimize lexicographically
            for k in range(len(group_indices)):
                result[group_indices[k]] = group_elements[k]
                
            # Move to the start of the next group
            i = j
            
        return result
