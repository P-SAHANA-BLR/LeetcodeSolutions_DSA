class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # The row always starts with 1
        row = [1]
        
        # Calculate each subsequent element dynamically using the combination formula
        for i in range(1, rowIndex + 1):
            # next_val = prev_val * (rowIndex - i + 1) / i
            # Use integer division to avoid float precision issues
            next_val = row[-1] * (rowIndex - i + 1) // i
            row.append(next_val)
            
        return row
