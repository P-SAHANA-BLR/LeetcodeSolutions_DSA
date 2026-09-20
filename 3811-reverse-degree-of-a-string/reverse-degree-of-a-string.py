class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        
        for idx, char in enumerate(s, start=1):
            # Calculate reversed alphabet position: 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            rev_alphabet_pos = 26 - (ord(char) - ord('a'))
            
            # Add the product of string index and reversed alphabet position
            total_degree += idx * rev_alphabet_pos
            
        return total_degree
