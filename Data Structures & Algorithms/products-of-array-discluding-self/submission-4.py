class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        ZeroCount = 0
        output = []

        for n in nums:
            if n == 0:
                total = total * 1
                ZeroCount = ZeroCount + 1
            else:
                total = n * total
                
        for n in nums:
            if ZeroCount == 1:
                if n != 0:
                    output.append(0)
                else:
                    output.append(total)
            elif ZeroCount > 1:
                output = [0] * len(nums)
                return output
            elif ZeroCount == 0:
                output.append(total//n)
        return output