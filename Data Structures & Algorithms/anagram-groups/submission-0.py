from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = defaultdict(list)
        for word in strs:
            temp_map = defaultdict(lambda: 0)
            for c in word:
                temp_map[c] += 1
            result_map[frozenset(temp_map.items())].append(word)
        return list(result_map.values())