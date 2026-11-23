class ProductOfNumbers:

    def __init__(self):
        # Initialize with 1 to handle division cleanly for full-length queries
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset the prefix products since any product including this 0 will be 0
            self.prefix = [1]
        else:
            # Append the running product
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is >= the number of valid non-zero elements tracked, a 0 was encountered
        if k >= len(self.prefix):
            return 0
        
        # Integer division gives the exact product of the last k elements
        return self.prefix[-1] // self.prefix[-1 - k]
