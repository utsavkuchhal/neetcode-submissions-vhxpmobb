import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(lambda: 0)
        for num in nums:
            freq_map[num] += 1
        pq = []
        for num, freq in freq_map.items():
            heapq.heappush(pq, (freq, num))
            if len(pq) > k:
                heapq.heappop(pq)
        result = []
        for item in pq:
            freq, num = item
            result.append(num)
        return result