class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Dictionary to store frequencies of characters in the current window
        char_counts = {}
        max_length = 0
        left = 0
        
        # Expand the window using the right pointer
        for right in range(len(s)):
            char = s[right]
            char_counts[char] = char_counts.get(char, 0) + 1
            
            # Shrink the window from the left if any character count exceeds 2
            while char_counts[char] > 2:
                char_counts[s[left]] -= 1
                left += 1
                
            # Update the maximum length of a valid substring
            max_length = max(max_length, right - left + 1)
            
        return max_length
