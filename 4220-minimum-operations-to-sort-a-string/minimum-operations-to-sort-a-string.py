from itertools import pairwise

class Solution:
    def minOperations(self, s: str) -> int:
        # Case 1: The string is already sorted
        if all(a <= b for a, b in pairwise(s)):
            return 0
        
        # Case 2: String length is 2 and it's unsorted (impossible to sort)
        if len(s) == 2:
            return -1
        
        # Find global minimum and maximum characters
        mn, mx = min(s), max(s)
        
        # Case 3: Min is at the front OR Max is at the back
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # Case 4: Min or Max is somewhere in the inner substring
        if any(c in (mn, mx) for c in s[1:-1]):
            return 2
            
        # Case 5: Worst case scenario where Min is only at the end and Max is only at the front
        return 3
