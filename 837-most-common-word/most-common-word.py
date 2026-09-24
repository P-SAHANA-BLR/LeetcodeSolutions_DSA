import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # Step 1: Replace all punctuation with spaces and convert to lowercase
        # This handles cases like "ball," or "bob,hit" cleanly
        normalized_str = re.sub(r"[!?',;.]", " ", paragraph).lower()
        
        # Step 2: Convert banned list to a set for O(1) lookups
        banned_set = set(banned)
        
        # Step 3: Split into words and filter out banned ones
        words = [word for word in normalized_str.split() if word not in banned_set]
        
        # Step 4: Count the words and return the most common one
        counts = Counter(words)
        return counts.most_common(1)[0][0]
