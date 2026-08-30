class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        # Step 1: Locate the indices of min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Step 2: Order them so i is always the smaller index
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        # Step 3: Compute deletions for all 3 valid strategies
        from_front = j + 1
        from_back = n - i
        from_both = (i + 1) + (n - j)
        
        # Return the most optimal approach
        return min(from_front, from_back, from_both)
