import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = []
        for stone in stones:
            heapq.heappush(min_heap, -stone)
        
        while len(min_heap) > 1:
            x = heapq.heappop(min_heap)
            y = heapq.heappop(min_heap)
            if x != y:
                heapq.heappush(min_heap, -abs(x - y))
        return -min_heap[0] if len(min_heap) else 0
