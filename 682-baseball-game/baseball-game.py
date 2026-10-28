class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        
        for op in operations:
            if op == '+':
                # Record a new score that is the sum of the previous two scores
                record.append(record[-1] + record[-2])
            elif op == 'D':
                # Record a new score that is the double of the previous score
                record.append(2 * record[-1])
            elif op == 'C':
                # Invalidate and remove the previous score
                record.pop()
            else:
                # Record a new integer score
                record.append(int(op))
                
        return sum(record)
