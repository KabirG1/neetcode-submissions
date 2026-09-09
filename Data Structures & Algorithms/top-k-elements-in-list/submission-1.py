class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        for i in nums:
            numFreq[i] = numFreq.get(i, 0) + 1

        for num, count in numFreq.items():
            freq[count].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        