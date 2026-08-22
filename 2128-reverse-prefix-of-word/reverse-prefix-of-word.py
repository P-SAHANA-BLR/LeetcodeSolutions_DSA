class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the first occurrence of ch
        idx = word.find(ch)
        
        # If ch is not found, .find() returns -1
        if idx == -1:
            return word
            
        # Reverse the prefix from 0 to idx, then add the rest of the string
        return word[:idx + 1][::-1] + word[idx + 1:]
