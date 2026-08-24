class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # Sum up 1 for every pattern that is found inside word
        return sum(1 for p in patterns if p in word)
