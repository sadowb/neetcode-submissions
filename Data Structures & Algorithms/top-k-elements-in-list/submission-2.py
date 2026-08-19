class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        result = dict(sorted(counts.items(),key = lambda n : n[1] ) )
        return list(result.keys())[-k:]
       