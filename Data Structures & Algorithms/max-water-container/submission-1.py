class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n= len (heights)
        maximum_volume = 0
        i = 0
        j = n - 1
        while i < j:
            volume = abs(j-i)*min(heights[i],heights[j])
            maximum_volume = max(volume,maximum_volume)
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
            

        return maximum_volume
