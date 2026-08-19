class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i just rembered the smart solution we used hashing 
        # but in a very smart way
        # first we create the hash to just keep track of the 
        # numbers that we saw in the array
        # then we check if we saw that number before
        # so what i would is calculate like 
        # let target = 7
        # and nums[i] + nums[j] == target
        # then what i only need to do is to find the number that will 
        #satisfy the condition 
        #it simply a calculation 
        # num[j] == target - num[i]
        seen = {}
        for i ,n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff],i]
            seen[n] = i
            #now in this case i am assinging the index to the it key value 

        # step 1
        # value is 3 
        # 7-3 = 4
        #seen = 4
        # it will skip the if loop and continue to the next number
        # seen = 4 , 3
        # now the value is 4 currently
        # now it will check if it has that value 
        # yes it will see that we have the value 4
        # then it will return the indices of the number 4
        # and it will also return the indices of the value that i have found in my hash table
