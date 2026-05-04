import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_dist = [float('inf')] * n
        min_heap = []
        heapq.heappush(min_heap, (0, 0)) # index, dist
        result = 0
        while min_heap:
            dist, node  = heapq.heappop(min_heap)
            if visited[node]:
                continue
            visited[node] = True
            result += dist
            for i in range(n):
                if not visited[i]:
                    dist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                    heapq.heappush(min_heap, (dist, i))
        return result