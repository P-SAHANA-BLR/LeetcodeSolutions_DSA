class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Function to calculate the sum of digits of a number
        def get_digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        n = len(nums)
        
        # Store elements along with their original indices and digit sums
        # Format: (digit_sum, value, original_index)
        arr = []
        for i, val in enumerate(nums):
            arr.append((get_digit_sum(val), val, i))
            
        # Sort based on:
        # 1. Digit sum (increasing order)
        # 2. Value itself (increasing order, if digit sums match)
        arr.sort()
        
        # Track visited elements to avoid counting elements in the same cycle multiple times
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct position, skip
            if visited[i] or arr[i][2] == i:
                continue
                
            # Calculate the cycle size
            cycle_size = 0
            curr = i
            
            while not visited[curr]:
                visited[curr] = True
                # Move to the index where the current element should go
                curr = arr[curr][2]
                cycle_size += 1
                
            # A cycle of length L requires L - 1 swaps
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps
