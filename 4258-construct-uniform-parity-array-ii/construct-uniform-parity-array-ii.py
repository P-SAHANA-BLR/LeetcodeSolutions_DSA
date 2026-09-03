class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Find the minimum odd number in nums1
        min_odd = min((x for x in nums1 if x % 2 != 0), default=None)
        
        # If there are no odd numbers, all numbers are even -> valid
        if min_odd is None:
            return True
            
        # Check if any even number is strictly less than the smallest odd number
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False
                
        return True
