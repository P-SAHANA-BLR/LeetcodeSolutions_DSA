class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    
        # Set pointers for nums1, nums2, and the placement position
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # Move backwards, placing the larger element at index p
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # If there are remaining elements in nums2, copy them
        # (Remaining elements in nums1 are already in place)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
