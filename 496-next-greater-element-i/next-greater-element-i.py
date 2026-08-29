class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Hash map to store the next greater element for each number in nums2
        mapping = {}
        stack = []
        
        # Linear scan to map next greater elements in nums2
        for num in nums2:
            # While stack is not empty and current num is greater than the stack's top
            while stack and num > stack[-1]:
                popped = stack.pop()
                mapping[popped] = num
            stack.append(num)
            
        # For remaining elements in stack, there is no next greater element (default to -1)
        # Construct the final answer array using O(1) lookups
        return [mapping.get(num, -1) for num in nums1]
