class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        
        # Helper function to find the greatest common divisor
        def get_gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
            
        # Precompute LCMs for all subsets using bitmasking
        subset_lcm = [0] * (1 << n)
        
        # Initialize base cases for single coins
        for i in range(n):
            subset_lcm[1 << i] = coins[i]
            
        # Compute LCM for all possible subsets
        for mask in range(1, 1 << n):
            low_bit = mask & -mask
            if mask != low_bit:
                prev_mask = mask ^ low_bit
                c1 = subset_lcm[prev_mask]
                c2 = subset_lcm[low_bit]
                # LCM(c1, c2) = (c1 * c2) / GCD(c1, c2)
                subset_lcm[mask] = (c1 * c2) // get_gcd(c1, c2)
                
        # Helper function to count unique multiples <= M using PIE
        def count_multiples(m: int) -> int:
            total = 0
            for mask in range(1, 1 << n):
                # Count set bits manually (Brian Kernighan's Algorithm)
                bits_count = 0
                temp = mask
                while temp:
                    temp &= temp - 1
                    bits_count += 1
                
                lcm_val = subset_lcm[mask]
                
                # Inclusion-Exclusion Principle logic
                if bits_count % 2 == 1:
                    total += m // lcm_val
                else:
                    total -= m // lcm_val
            return total

        # Define Binary Search boundaries
        # Find minimum value using a loop to avoid min() built-in overhead if desired,
        # though built-in min() is standard and requires no imports.
        min_coin = coins[0]
        for coin in coins:
            if coin < min_coin:
                min_coin = coin
                
        low = min_coin
        high = min_coin * k
        ans = high
        
        # Perform Binary Search
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1  # Look for a smaller valid amount
            else:
                low = mid + 1   # Increase our lower search bound
                
        return ans
