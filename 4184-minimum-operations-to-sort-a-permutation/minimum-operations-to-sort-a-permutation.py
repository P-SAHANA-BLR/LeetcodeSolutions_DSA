class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        # Find the index where 0 is located
        idx0 = nums.index(0)
        
        # Check Case 1: Direct (Increasing) Cyclic Shift
        is_increasing_cyclic = True
        for i in range(n):
            if nums[(idx0 + i) % n] != i:
                is_increasing_cyclic = False
                break
                
        if is_increasing_cyclic:
            # Path A: Only rotations -> idx0
            # Path B: Reverse -> Rotate -> Reverse -> 2 + ((n - idx0) % n)
            return min(idx0, 2 + ((n - idx0) % n))
            
        # Check Case 2: Reversed (Decreasing) Cyclic Shift
        is_decreasing_cyclic = True
        for i in range(n):
            if nums[(idx0 - i) % n] != i:
                is_decreasing_cyclic = False
                break
                
        if is_decreasing_cyclic:
            # Path A: Reverse -> Rotate -> n - idx0
            # Path B: Rotate -> Reverse -> ((idx0 + 1) % n) + 1
            return min(n - idx0, ((idx0 + 1) % n) + 1)
            
        return -1
