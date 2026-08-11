class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present_set = set(nums)
        start = min(nums)
        end = max(nums)
        missing = []
        for x in range(start + 1, end):
            if x not in present_set:
                missing.append(x)
        return missing
