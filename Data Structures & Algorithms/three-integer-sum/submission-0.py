

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []
        
        for i in range(n):
            # If the current number is greater than 0, break out of the loop
            if nums[i] > 0:
                break
            # Skip duplicate elements for the first number in the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            low, high = i + 1, n - 1
            
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                
                if total == 0:
                    # Add the triplet to the answer
                    answer.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    # Skip duplicate elements for the second and third numbers
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif total > 0:
                    high -= 1
                else:
                    low += 1
        
        return answer

            

        
