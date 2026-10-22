class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        # Dictionary to map bucket_id -> number
        buckets = {}
        
        # The width of each bucket
        width = valueDiff + 1
        
        for i, num in enumerate(nums):
            # Calculate the bucket ID for the current number
            bucket_id = num // width
            
            # Condition 1: Same bucket contains a number -> difference <= valueDiff
            if bucket_id in buckets:
                return True
            
            # Condition 2: Check the left adjacent bucket
            if (bucket_id - 1) in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
                
            # Condition 3: Check the right adjacent bucket
            if (bucket_id + 1) in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            # Insert the current number into its bucket
            buckets[bucket_id] = num
            
            # Maintain the sliding window size of indexDiff
            if i >= indexDiff:
                # Remove the element that is sliding out of the window bounds
                old_bucket_id = nums[i - indexDiff] // width
                del buckets[old_bucket_id]
                
        return False
