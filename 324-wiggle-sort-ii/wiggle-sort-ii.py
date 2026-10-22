class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Create a sorted copy of the numbers
        sorted_nums = sorted(nums)
        
        # Step 2: Find the midpoint to split smaller and larger elements
        # (n + 1) // 2 ensures the smaller half gets the extra element if n is odd
        mid = (len(nums) + 1) // 2
        
        # Step 3: Distribute elements backwards into alternating slots
        # Even positions take the smaller half in reverse order
        nums[::2] = sorted_nums[:mid][::-1]
        
        # Odd positions take the larger half in reverse order
        nums[1::2] = sorted_nums[mid:][::-1]
