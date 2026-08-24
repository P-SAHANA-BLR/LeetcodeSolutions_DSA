class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            # Calculate total weight of the current word
            total_weight = sum(weights[ord(char) - ord('a')] for char in word)
            
            # Take modulo 26
            rem = total_weight % 26
            
            # Map to reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a')
            mapped_char = chr(ord('a') + (25 - rem))
            result.append(mapped_char)
            
        return "".join(result)
