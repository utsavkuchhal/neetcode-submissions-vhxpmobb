from functools import cmp_to_key

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final_output = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for start, end in intervals:
            if not final_output:
                final_output.append([start, end])
            else:
                last_start, last_end = final_output[-1]
                if start > last_end:
                    final_output.append([start, end])
                elif last_start <= start < end or last_end == start:
                    final_output[-1][1] = max(end, last_end)
        return final_output
