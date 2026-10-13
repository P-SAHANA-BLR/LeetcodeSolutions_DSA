class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Calculate the squares and sort them in ascending order
        squares = sorted(x * x for x in nums)
        
        # The first n // 2 smallest elements get a minus sign
        mid = len(squares) // 2
        
        # Sum the upper half and subtract the lower half
        return sum(squares[mid:]) - sum(squares[:mid])
