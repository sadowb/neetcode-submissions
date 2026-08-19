class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ok i already know the solution but how to solve it in o(n)
        # that the problem 
        # let at least solve the problem using division then think about 
        # follow up and i tghaught of a very clever one 
        # where if i saw any zero then i need to start applying 0 to all the other arrays 
        # basically division
        res = 1
        output = []
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                res *= num
        
        print(res)
      
        for num in nums:
            if zero_count > 1:
                output.append(0)
            elif zero_count == 1:
                if num == 0:
                    output.append(res)
                else:
                    output.append(0)
            else:
                output.append(int(res/num))
        
        return output
