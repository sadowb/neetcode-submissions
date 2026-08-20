# so this approach didnt work because it didnt account that the solution needs to keep the original indexes in here that why it didnt work and one way to solve it is to keep the original index and sort 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(enumerate(nums))
        nums = sorted(nums, key=lambda x: x[1])
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i][1] + nums[j][1] == target:
                return [min(nums[i][0],nums[j][0]),max(nums[i][0],nums[j][0])]
            elif nums[i][1] + nums[j][1] < target:
                i = i + 1
            else:
                j = j - 1
        
            