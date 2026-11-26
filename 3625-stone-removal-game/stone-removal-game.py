class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_to_remove = 10
        a_turn = True #a_turn -> Alice's turn 
        
        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
            a_turn = not a_turn
            
        # If the loop breaks on Bob's turn (Alice's turn is False), Bob cannot move and Alice wins.
        return not a_turn
