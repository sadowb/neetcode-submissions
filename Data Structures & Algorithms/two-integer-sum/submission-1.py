class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i would use the two pointer strategy meaning that i would take the first pointer and another pointer and keep going to the center 
        # and to take that power i need to sort them for it to work 
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if (nums[i]+nums[j] == target):
                    return [i,j]

            


       