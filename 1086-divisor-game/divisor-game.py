class Solution:
    def divisorGame(self, n: int) -> bool:
        # Alice wins if and only if the starting number is even
        return n % 2 == 0
