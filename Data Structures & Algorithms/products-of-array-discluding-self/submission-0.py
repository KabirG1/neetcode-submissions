class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [0] * length
        pref = [0] * length
        suff = [0] * length

        pref[0] = 1
        suff[length - 1] = 1

        for i in range(1, length):
            pref[i] = nums[i - 1] * pref[i - 1]

        for i in range(length - 2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]
        
        for i in range(0, length):
            output[i] = pref[i] * suff[i]

        return output
