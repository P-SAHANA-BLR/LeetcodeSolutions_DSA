class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_string: str, left: int, right: int):
            # Base case: if the current string reaches the maximum length, it's valid
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Rule 1: We can add an open parenthesis if we still have some left
            if left < n:
                backtrack(current_string + "(", left + 1, right)
                
            # Rule 2: We can add a close parenthesis if it matches a previous open one
            if right < left:
                backtrack(current_string + ")", left, right + 1)
                
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result
