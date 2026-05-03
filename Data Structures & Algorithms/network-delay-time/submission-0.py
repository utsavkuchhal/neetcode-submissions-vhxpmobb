from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, weight in times:
            graph[u].append((v, weight))

        min_heap = []
        distance = [float('inf')] * (n + 1)
        distance[k] = 0
        heapq.heappush(min_heap, (0, k))
        while min_heap:
            dist, node = heapq.heappop(min_heap)
            for neighbour, n_dist in graph[node]:
                if dist + n_dist < distance[neighbour]:
                    distance[neighbour] = dist + n_dist
                    heapq.heappush(min_heap, (distance[neighbour], neighbour))
        print(distance)
        return max(distance[1:]) if max(distance[1:]) != float('inf') else -1
            