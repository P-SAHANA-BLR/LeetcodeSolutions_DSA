class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Convert list to set for O(1) lookups
        num_set = set(nums)
        
        # Start checking from the first positive multiple of k
        multiple = k
        
        # Keep incrementing by k until a multiple is missing
        while multiple in num_set:
            multiple += k
            
        return multiple
