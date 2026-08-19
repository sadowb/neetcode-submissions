class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_number = {}
        for i in range(len(nums)):
            frequent_number[nums[i]] = 1 + frequent_number.get(nums[i], 0)
        
        # Sort the dictionary items by value (frequency) in descending order
        sorted_list = sorted(frequent_number.items(), key=lambda item: item[1], reverse=True)
        
        # Extract the keys (numbers) from the sorted list
        sorted_keys = [key for key, value in sorted_list]
        
        # Initialize result list
        result = []
        i = 0  # Initialize the counter
        
        # Append the top k keys to the result
        while i < k:
            result.append(sorted_keys.pop(0))  # Pop the first key
            i += 1
        
        return result
        

        
                