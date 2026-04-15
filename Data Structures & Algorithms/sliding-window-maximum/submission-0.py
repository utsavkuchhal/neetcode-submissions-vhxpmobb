import heapq
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        max_heap = []
        index_map = {}
        for i in range(k):
            index_map[i] = 1
            heapq.heappush(max_heap, (-nums[i], i))

        ans.append(-max_heap[0][0])
        print(ans)
        left = 0
        for i in range(k, len(nums)):
            del index_map[left]
            index_map[i] = 1
            heapq.heappush(max_heap, (-nums[i], i))
            while max_heap[0][1] not in index_map:
                heapq.heappop(max_heap)
            ans.append(-max_heap[0][0])
            left += 1
        return ans
            

