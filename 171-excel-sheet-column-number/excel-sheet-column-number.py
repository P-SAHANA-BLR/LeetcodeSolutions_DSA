class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for char in columnTitle:
            # ord('A') is 65. Subtracting 64 gives: 'A' -> 1, 'B' -> 2, etc.
            value = ord(char) - 64
            ans = ans * 26 + value
        return ans
