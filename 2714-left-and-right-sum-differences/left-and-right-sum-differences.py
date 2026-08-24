class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        answer = []
        
        for num in nums:
            # right_sum should exclude the current element
            right_sum -= num
            
            # Append the absolute difference
            answer.append(abs(left_sum - right_sum))
            
            # left_sum accumulates the current element for subsequent indices
            left_sum += num
            
        return answer
