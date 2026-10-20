class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # 1. Precalculate prefix maximums and suffix minimums
        pref_max = [0] * n
        suff_min = [0] * n
        
        pref_max[0] = nums[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i - 1], nums[i])
            
        suff_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])
            
        # 2. Count global adjacent drops (descending pairs)
        # drops[i] tells us if nums[i] > nums[i+1]
        drops = [0] * n
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                drops[i] = 1
                
        # Build prefix sums of drops to query number of drops in O(1) time
        pref_drops = [0] * (n + 1)
        for i in range(n):
            pref_drops[i + 1] = pref_drops[i] + drops[i]

        # Helper function to check if a specific divisor k is valid
        def is_valid(k: int) -> bool:
            # Check inter-block validity: max of block j <= min of block j+1
            for j in range(0, n - k, k):
                block_max = pref_max[j + k - 1]
                next_block_min = suff_min[j + k]
                if block_max > next_block_min:
                    return False
                    
            # Check intra-block validity: each block must have at most 1 drop circularly
            for j in range(0, n, k):
                # Internal drops from j to j + k - 2
                internal_drops = pref_drops[j + k - 1] - pref_drops[j]
                
                # Circular wrap drop from the last element to the first element of the block
                wrap_drop = 1 if nums[j + k - 1] > nums[j] else 0
                
                if internal_drops + wrap_drop > 1:
                    return False
                    
            return True

        # 3. Find all divisors k of n and sum up the valid ones
        ans = 0
        for k in range(1, int(n**0.5) + 1):
            if n % k == 0:
                if is_valid(k):
                    ans += k
                # Check the pair divisor if it's different
                if k * k != n:
                    if is_valid(n // k):
                        ans += n // k
                        
        return ans
