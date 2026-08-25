class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        # Step 1: Sort to place duplicate elements next to each other
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack():
            # Base case: if path length matches nums length, a valid permutation is formed
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                # If the element is already used in the current path, skip it
                if used[i]:
                    continue
                
                # If it's a duplicate and the previous duplicate wasn't used yet, skip it
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # Make choices
                used[i] = True
                path.append(nums[i])
                
                # Backtrack
                backtrack()
                
                # Undo choices
                path.pop()
                used[i] = False
                
        backtrack()
        return res
