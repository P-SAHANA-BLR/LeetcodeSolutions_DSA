class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Sort the array to easily find the median
        nums.sort()
        
        # The median is the middle element
        median = nums[len(nums) // 2]
        
        # Calculate the total moves required to bring all elements to the median
        moves = sum(abs(num - median) for num in nums)
        
        return moves
