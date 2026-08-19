class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n= len (heights)
        maximum_volume = 0
        for i in range (n):
            for j in range(i+1,n):
                height = min(heights[i],heights[j])
                distance = abs(i - j)
                volume = distance * height
                maximum_volume = max(volume,maximum_volume)
        maximum_volume = max(volume,maximum_volume)
        return maximum_volume
