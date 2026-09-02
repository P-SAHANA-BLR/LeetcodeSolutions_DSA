from collections import deque

class MyStack:

    def __init__(self):
        # Initialize a single queue using deque
        self.q = deque()

    def push(self, x: int) -> None:
        # Get the current size before adding the new element
        size = len(self.q)
        # Push the element to the back of the queue
        self.q.append(x)
        # Rotate all previous elements to the back
        for _ in range(size):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # The top element is already at the front of the queue
        return self.q.popleft()

    def top(self) -> int:
        # The top element is at the front of the queue
        return self.q[0]

    def empty(self) -> bool:
        # Check if the queue contains any elements
        return len(self.q) == 0
