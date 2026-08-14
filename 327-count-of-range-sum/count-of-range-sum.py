class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Create the prefix sum array starting with 0
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
            
        def count_while_merge_sort(left: int, right: int) -> int:
            if right - left <= 1:
                return 0
                
            mid = (left + right) // 2
            # Count valid ranges entirely within the left or right halves
            count = count_while_merge_sort(left, mid) + count_while_merge_sort(mid, right)
            
            # Count valid ranges crossing the midpoint
            j_lower = mid
            j_upper = mid
            
            for i in range(left, mid):
                # Move j_lower to the first index where prefix_sums[j] - prefix_sums[i] >= lower
                while j_lower < right and prefix_sums[j_lower] - prefix_sums[i] < lower:
                    j_lower += 1
                # Move j_upper to the first index where prefix_sums[j] - prefix_sums[i] > upper
                while j_upper < right and prefix_sums[j_upper] - prefix_sums[i] <= upper:
                    j_upper += 1
                
                # The number of valid j indices for this specific i
                count += (j_upper - j_lower)
                
            # Perform standard merge step to keep the prefix_sums segment sorted
            prefix_sums[left:right] = sorted(prefix_sums[left:right])
            return count

        return count_while_merge_sort(0, len(prefix_sums))
