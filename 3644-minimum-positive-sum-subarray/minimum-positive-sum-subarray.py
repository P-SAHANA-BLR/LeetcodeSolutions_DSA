from typing import List


class Solution:

  def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
    n = len(nums)
    min_sum = float('inf')

    for i in range(n - l + 1):
      current_sum = 0
      # Extend subarray up to maximum allowed length r or end of array
      for j in range(i, min(n, i + r)):
        current_sum += nums[j]
        # Check if subarray length is within [l, r] and sum is positive
        if j - i + 1 >= l and current_sum > 0:
          if current_sum < min_sum:
            min_sum = current_sum

    return min_sum if min_sum != float('inf') else -1
