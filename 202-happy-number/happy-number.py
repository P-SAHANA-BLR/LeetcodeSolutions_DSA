class Solution:
    def isHappy(self, n: int) -> bool:
        # Helper function to calculate the sum of the squares of digits
        def get_next(num: int) -> int:
            total_sum = 0
            while num > 0:
                digit = num % 10
                total_sum += digit * digit
                num //= 10
            return total_sum
            
        # Initialize two pointers (slow moves 1 step, fast moves 2 steps)
        slow = n
        fast = get_next(n)
        
        # Loop until they meet or fast hits 1
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            
        return fast == 1
