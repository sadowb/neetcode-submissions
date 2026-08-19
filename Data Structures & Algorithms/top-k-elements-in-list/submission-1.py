class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)
        for num in nums:
            result[num] += 1
        result = dict(sorted(result.items(), key=lambda item: item[1]))
        return list(result.keys())[-k:]

        
                