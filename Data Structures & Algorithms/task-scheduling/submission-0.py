import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = Counter(tasks)
        freq_list = [-value for value in freq_map.values()]
        heapq.heapify(freq_list)
        waiting_list = deque([])
        time = 0
        while freq_list or waiting_list:
            time += 1
            if waiting_list and waiting_list[0][1] == time:
                count, _ = waiting_list.popleft()
                heapq.heappush(freq_list, count)
            if freq_list:
                count = heapq.heappop(freq_list)
                count += 1
                if count:
                    waiting_list.append((count, time + n + 1))
        return time