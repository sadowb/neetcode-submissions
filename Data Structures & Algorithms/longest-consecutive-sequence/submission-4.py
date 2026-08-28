class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longestSequence = 0
        if len(nums) == 0:
            return 0
        for num in mySet:
            # this evaluates to true if the value that i have doesnt exist it means that this is the smallest number in the array
            if (num - 1) not in mySet:
                currentNumber = num + 1
                currentLenght = 0

                while currentNumber in mySet:
                    currentLenght += 1
                    currentNumber += 1
                    longestSequence = max(currentLenght,longestSequence)
            
        return longestSequence + 1
                