class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: the 1st element is always "1"
        current_str = "1"
        
        # Iteratively generate the sequence up to the nth element
        for _ in range(1, n):
            next_str = []
            i = 0
            
            # Perform Run-Length Encoding (RLE) on the current string
            while i < len(current_str):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(current_str) and current_str[i] == current_str[i + 1]:
                    count += 1
                    i += 1
                
                # Append the count followed by the character itself
                next_str.append(str(count))
                next_str.append(current_str[i])
                i += 1
            
            # Move to the next string in the sequence
            current_str = "".join(next_str)
            
        return current_str
