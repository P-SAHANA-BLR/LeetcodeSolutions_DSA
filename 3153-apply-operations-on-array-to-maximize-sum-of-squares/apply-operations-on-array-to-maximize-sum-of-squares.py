class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Count the frequency of set bits at each position
        bit_counts = [0] * 32
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bit_counts[i] += 1
        
        ans = 0
        
        # Construct the top k largest numbers greedily
        for _ in range(k):
            current_num = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            
            # Add the square of the constructed number to the answer
            ans = (ans + current_num * current_num) % MOD
            
        return ans
