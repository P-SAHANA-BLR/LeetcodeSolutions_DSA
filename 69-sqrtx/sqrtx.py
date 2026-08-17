class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        left, right = 2, x // 2
        ans = 1
        
        while left <= right:
            mid = left + (right - left) // 2
            num_sq = mid * mid
            
            if num_sq == x:
                return mid
            elif num_sq < x:
                ans = mid       # Store mid as a potential candidate for rounding down
                left = mid + 1  # Try to find a larger value
            else:
                right = mid - 1 # Reduce the search space
                
        return ans
