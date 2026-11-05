import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # Sort arr2 to enable binary search
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Find the insertion point for the lower bound (x - d)
            idx = bisect.bisect_left(arr2, x - d)
            
            # If idx is within bounds and the element is within the upper bound (x + d)
            # then |x - arr2[idx]| <= d holds true.
            if idx < len(arr2) and arr2[idx] <= x + d:
                continue
                
            # If no element in arr2 falls in [x - d, x + d], increment count
            distance_value += 1
            
        return distance_value
