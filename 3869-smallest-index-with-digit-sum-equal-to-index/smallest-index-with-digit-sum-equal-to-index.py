class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            # Calculate the sum of digits of num
            digit_sum = 0
            temp = num
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            
            # Check if the sum of digits equals the current index
            if digit_sum == i:
                return i
                
        return -1
