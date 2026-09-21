class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        # dp[r] tracks the count of subarrays ending at the previous position 
        # whose product modulo k equals r
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            
            # 1. Start a new subarray consisting solely of the current element
            new_dp[num_mod] += 1
            
            # 2. Extend all existing subarrays that ended at the previous element
            for i in range(k):
                if dp[i] > 0:
                    new_mod = (i * num_mod) % k
                    new_dp[new_mod] += dp[i]
            
            # 3. Accumulate the counts from the current position into the final answer
            for r in range(k):
                ans[r] += new_dp[r]
                
            dp = new_dp
            
        return ans
