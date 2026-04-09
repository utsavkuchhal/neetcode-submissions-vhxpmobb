from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.times_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        times = self.times_map[key]
        n = len(times)
        # if n == 1:
        #     return times[0][1] if timestamp >= times[0][0] else ""

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if times[mid][0] == timestamp:
                return times[mid][1]
            elif times[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        return times[right][1] if right >= 0 else ""