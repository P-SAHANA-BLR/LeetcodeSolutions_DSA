class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def max_heapify(n: int, i: int):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            # Check if left child exists and is greater than root
            if left < n and nums[left] > nums[largest]:
                largest = left
                
            # Check if right child exists and is greater than largest so far
            if right < n and nums[right] > nums[largest]:
                largest = right
                
            # Change root if needed
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]  # swap
                # Recursively heapify the affected sub-tree
                max_heapify(n, largest)

        n = len(nums)
        
        # Build a maxheap. 
        # Traverse from the last non-leaf node up to the root.
        for i in range(n // 2 - 1, -1, -1):
            max_heapify(n, i)
            
        # One by one extract elements from the heap
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]  # swap current root to the end
            max_heapify(i, 0)                    # call max heapify on the reduced heap
            
        return nums
