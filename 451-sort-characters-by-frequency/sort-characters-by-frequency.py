from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        counts = Counter(s)
        
        # Step 2 & 3: Sort by frequency in descending order and build the result
        # most_common() returns a list of (character, frequency) sorted by frequency
        result = []
        for char, freq in counts.most_common():
            result.append(char * freq)
            
        return "".join(result)
