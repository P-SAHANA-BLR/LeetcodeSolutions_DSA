class Solution:
    def checkValidString(self, s: str) -> bool:
        # cmin and cmax represent the range of possible open '(' parentheses
        cmin = 0
        cmax = 0
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            elif char == '*':
                cmin -= 1  # if treated as ')'
                cmax += 1  # if treated as '('
            
            # If max possible open brackets is negative, we have too many ')'
            if cmax < 0:
                return False
            
            # cmin cannot be less than 0 because we can choose to treat '*' as "" instead of ')'
            if cmin < 0:
                cmin = 0
                
        # If the minimum possible open brackets is 0, the string is valid
        return cmin == 0
