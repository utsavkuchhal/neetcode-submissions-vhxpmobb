"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        min_heap = []
        meeting_rooms = 0
        for index in range(0, len(intervals)):
            meeting_rooms = max(meeting_rooms, len(min_heap))
            while min_heap and min_heap[0] <= intervals[index].start:
                 heapq.heappop(min_heap)
            heapq.heappush(min_heap, intervals[index].end)
        return max(meeting_rooms, len(min_heap))
