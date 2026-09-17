class MinStack:

    def __init__(self):
        # The stack will store tuples of (val, min_val_at_this_point)
        self.stack = []

    def push(self, value: int) -> None:
        if not self.stack:
            # If the stack is empty, the current value is the minimum
            self.stack.append((value, value))
        else:
            # Compare current value with the minimum of the previous state
            current_min = self.stack[-1][1]
            self.stack.append((value, min(value, current_min)))

    def pop(self) -> None:
        # Standard stack pop operation
        self.stack.pop()

    def top(self) -> int:
        # Return the actual value at the top of the stack
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the minimum value recorded at the top state
        return self.stack[-1][1]
