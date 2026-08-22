class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        counterFrequency = defaultdict(int)
        for n in nums:
            counterFrequency[n] += 1
        # now let build the list to like heapify the thing to how many it occured
        for number , frequency in counterFrequency.items():
            heapq.heappush(heap,(-frequency,number))
        for _ in range(k):
            frequency,number = heapq.heappop(heap)
            result.append(number)

        return result