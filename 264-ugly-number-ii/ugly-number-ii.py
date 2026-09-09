class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Array to store the first n ugly numbers
        ugly = [0] * n
        ugly[0] = 1  # The first ugly number is 1
        
        # Pointers for multiples of 2, 3, and 5
        p2 = p3 = p5 = 0
        
        for i in range(1, n):
            # Generate candidates for the next ugly number
            next_2 = ugly[p2] * 2
            next_3 = ugly[p3] * 3
            next_5 = ugly[p5] * 5
            
            # The next ugly number is the smallest among the candidates
            next_ugly = min(next_2, next_3, next_5)
            ugly[i] = next_ugly
            
            # Move the pointer forward for the choice(s) that matched next_ugly
            if next_ugly == next_2:
                p2 += 1
            if next_ugly == next_3:
                p3 += 1
            if next_ugly == next_5:
                p5 += 1
                
        return ugly[-1]
