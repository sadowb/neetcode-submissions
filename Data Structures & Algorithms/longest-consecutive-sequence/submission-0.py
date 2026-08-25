class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longestSequence = 0
        currentLength = 0
        for n in mySet:
            if (n - 1) not in mySet:
                Number = n
                currentLength = 1
                while Number + 1 in mySet:
                    Number += 1
                    currentLength += 1
                longestSequence = max(longestSequence,currentLength)
        return longestSequence
                
        