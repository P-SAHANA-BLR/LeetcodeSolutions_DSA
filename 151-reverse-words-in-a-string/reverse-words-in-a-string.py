class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string by words (automatically handles multiple spaces)
        words = s.split()
        
        # Step 2: Reverse the list of words
        words.reverse()
        
        # Step 3: Join the words back together with a single space
        return " ".join(words)
