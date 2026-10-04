class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Find the last occurrence index of each character
        last_idx = {char: i for i, char in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            # If the character is already in our result stack, skip it
            if char in seen:
                continue
                
            # Maintain the lexicographical order (monotonic stack property)
            # Pop characters from stack if they are larger than current char 
            # AND they appear again later in the string
            while stack and stack[-1] > char and last_idx[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
            
            # Add the current character to the stack and seen set
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
