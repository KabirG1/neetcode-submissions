class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDups = set(nums)
        if (len(nums) == len(noDups)):
            return False
        return True