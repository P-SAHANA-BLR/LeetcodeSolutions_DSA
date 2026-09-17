class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        m, n = len(nums1), len(nums2)
        best_combination = []
        
        # Helper 1: Extract the largest subsequence of length `size` from an array
        def getMaxSubsequence(nums: list[int], size: int) -> list[int]:
            stack = []
            drop_count = len(nums) - size  # Total elements we are allowed to discard
            
            for digit in nums:
                # Maintain monotonic decreasing stack behavior while we still have drops available
                while drop_count > 0 and stack and stack[-1] < digit:
                    stack.pop()
                    drop_count -= 1
                stack.append(digit)
                
            return stack[:size]
        
        # Helper 2: Merge two subsequences to maximize the combined number lexicographically
        def mergeSubsequences(sub1: list[int], sub2: list[int]) -> list[int]:
            result = []
            i, j = 0, 0
            
            while i < len(sub1) or j < len(sub2):
                # Python's slice comparison automatically checks lexicographical order
                if sub1[i:] > sub2[j:]:
                    result.append(sub1[i])
                    i += 1
                else:
                    result.append(sub2[j])
                    j += 1
                    
            return result
        
        # Explore all valid splits of k elements between nums1 and nums2
        # i represents the number of elements picked from nums1
        start_i = max(0, k - n)
        end_i = min(k, m)
        
        for i in range(start_i, end_i + 1):
            sub1 = getMaxSubsequence(nums1, i)
            sub2 = getMaxSubsequence(nums2, k - i)
            candidate = mergeSubsequences(sub1, sub2)
            
            # Keep the globally maximum sequence found
            if candidate > best_combination:
                best_combination = candidate
                
        return best_combination
