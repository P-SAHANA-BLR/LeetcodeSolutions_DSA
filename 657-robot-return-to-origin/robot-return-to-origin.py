class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # The robot returns to origin if vertical and horizontal moves cancel out
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
