class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = {}
        for i, num in enumerate(nums):
            nums1[num] = i
        
        for i, num in enumerate(nums):
            diff = target-num
            if (diff in nums1 and nums1[diff] != i):
                return [i, nums1[diff]]
        return []