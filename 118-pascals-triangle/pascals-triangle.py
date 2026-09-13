class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the triangle with the first row
        triangle = [[1]]
        
        # Build the remaining rows up to numRows
        for i in range(1, numRows):
            prev_row = triangle[-1]
            # Every row starts with a 1
            new_row = [1]
            
            # Generate the middle elements by summing adjacent elements from the previous row
            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])
                
            # Every row ends with a 1
            new_row.append(1)
            triangle.append(new_row)
            
        return triangle
