class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i < j:
        
            current = numbers[i] + numbers[j]
            if current > target:
                j -= 1
            elif target > current:
                i += 1
            elif current == target :
                return [i+1,j+1]
           
