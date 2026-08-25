class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        # Containers to store counts or segments of characters
        count_y = 0
        count_x = 0
        others = []
        
        # Partition the characters into the three blocks
        for char in s:
            if char == y:
                count_y += 1
            elif char == x:
                count_x += 1
            else:
                others.append(char)
                
        # Reconstruct the string by placing all 'y's first, then 'others', then 'x's
        return (y * count_y) + "".join(others) + (x * count_x)
