class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        water = 0

        while (right > left):
            tempWater = (right - left) * min(heights[left], heights[right])
            water = tempWater if (tempWater > water) else water
            if (heights[right] > heights[left]):
                left += 1
            else:
                right -= 1
        return water