from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occourance_map = defaultdict(lambda: float('-inf'))
        for index, char in enumerate(s):
            last_occourance_map[char] = max(last_occourance_map[char], index)
        result = []
        index = 0
        while index < len(s):
            last_index = last_occourance_map[s[index]]
            start = index
            while index < last_index:
                last_index = max(last_index, last_occourance_map[s[index]])
                index += 1
            result.append(last_index - start + 1)
            index += 1
        return result