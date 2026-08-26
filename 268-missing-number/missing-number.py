class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Calculate the sum of numbers from 0 to n
        expected_sum = (n * (n + 1)) // 2
        # Calculate the actual sum of the elements in the array
        actual_sum = sum(nums)
        
        # The difference is the missing number
        return expected_sum - actual_sum
