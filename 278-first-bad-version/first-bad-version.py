# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        
        while low < high:
            # Prevent potential overflow in languages like C++/Java, 
            # though Python handles arbitrarily large integers automatically
            mid = low + (high - low) // 2
            
            if isBadVersion(mid):
                # mid is bad, the first bad version could be mid or to the left
                high = mid
            else:
                # mid is good, the first bad version must be strictly to the right
                low = mid + 1
                
        # low and high converge to the first bad version
        return low

