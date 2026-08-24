class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Create a set of all unique characters present in the word
        char_set = set(word)
        special_count = 0
        
        # Iterate through all lowercase alphabet characters
        for i in range(26):
            lower_char = chr(ord('a') + i)
            upper_char = chr(ord('A') + i)
            
            # If both cases exist in our set, it's a special character
            if lower_char in char_set and upper_char in char_set:
                special_count += 1
                
        return special_count
