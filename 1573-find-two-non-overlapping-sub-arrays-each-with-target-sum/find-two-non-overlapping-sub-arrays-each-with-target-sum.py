class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # min_len[i] stores the minimum length of a valid sub-array in arr[0...i]
        min_len = [float('inf')] * n
        
        left = 0
        current_sum = 0
        min_total_sum = float('inf')
        best_left_len = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window if the sum exceeds the target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
                
            # If we found a valid sub-array ending at `right`
            if current_sum == target:
                current_len = right - left + 1
                
                # Check if there is a valid non-overlapping sub-array to the left
                if left > 0 and min_len[left - 1] != float('inf'):
                    min_total_sum = min(min_total_sum, current_len + min_len[left - 1])
                
                # Update the best length found up to the current right pointer
                best_left_len = min(best_left_len, current_len)
            
            # Carry over the best length seen so far to the DP array
            min_len[right] = best_left_len
            
        return min_total_sum if min_total_sum != float('inf') else -1
