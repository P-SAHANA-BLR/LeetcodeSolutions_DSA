class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_sort(left: int, right: int) -> int:
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            # Count reverse pairs in left half, right half, and across both halves
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)
            
            # Count reverse pairs across the split (Left[i] > 2 * Right[j])
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
            
            # Standard merge step to maintain sorted order
            nums[left:right + 1] = sorted(nums[left:right + 1])
            return count

        return merge_sort(0, len(nums) - 1)
