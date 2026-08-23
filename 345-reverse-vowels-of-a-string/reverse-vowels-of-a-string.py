class Solution:
    def reverseVowels(self, s: str) -> str:
        # Use a set for O(1) fast lookup membership tests
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        # Convert string to a mutable list of characters
        chars = list(s)
        
        left, right = 0, len(chars) - 1
        
        while left < right:
            # Move the left pointer until we find a vowel
            while left < right and chars[left] not in vowels:
                left += 1
                
            # Move the right pointer until we find a vowel
            while left < right and chars[right] not in vowels:
                right -= 1
                
            # Swap the vowels
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
                
        # Join characters back into a string
        return "".join(chars)
