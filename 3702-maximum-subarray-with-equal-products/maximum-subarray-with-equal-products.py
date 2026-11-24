import math
from typing import List


class Solution:

  def maxLength(self, nums: List[int]) -> int:
    n = len(nums)
    max_len = 1  # Any single element subarray is trivially product equivalent

    # Upper bound for lcm(1..10) * max(nums) = 2520 * 10 = 25200
    MAX_BOUND = 25200

    for i in range(n):
      curr_prod = 1
      curr_gcd = 0
      curr_lcm = 1

      for j in range(i, n):
        curr_prod *= nums[j]

        # Early exit if product exceeds the maximum possible lcm * gcd
        if curr_prod > MAX_BOUND:
          break

        curr_gcd = math.gcd(curr_gcd, nums[j])
        curr_lcm = math.lcm(curr_lcm, nums[j])

        if curr_prod == curr_lcm * curr_gcd:
          max_len = max(max_len, j - i + 1)

    return max_len

