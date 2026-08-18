from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets and find their common elements
        return list(set(nums1) & set(nums2))
