class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # If count reaches 0, we select a new candidate
            if count == 0:
                candidate = num
            
            # Adjust count based on whether the current number matches the candidate
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate
