class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = len(nums) * [1]
        prefix = 1
        n = len(nums)
        # let calculate the prefix 
        for i in range(n):
            prefix_product[i] = prefix
            prefix = nums[i] * prefix
        # let calculate the suffix 
        suffix_product = [1] * len(nums)
        suffix = 1
        for i in range(n-1,-1,-1):
            suffix_product[i] = suffix
            suffix = nums[i] * suffix
        product = [1] * len(nums)
        for i in range(n):
            product[i] = suffix_product[i] * prefix_product[i]
        return product
