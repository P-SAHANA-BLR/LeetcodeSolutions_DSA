from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map to store grouped anagrams: { sorted_string : [original_strings] }
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sorting the string creates a unique signature for the anagram group
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
            
        # Return all grouped lists
        return list(anagram_map.values())
