import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap, (-dist, [x, y]))
            while len(min_heap) > k:
                heapq.heappop(min_heap)
        ans = []
        while min_heap:
            _, point = heapq.heappop(min_heap)
            ans.append(point)
        return ans