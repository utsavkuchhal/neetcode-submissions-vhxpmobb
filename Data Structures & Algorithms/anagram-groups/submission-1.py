from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = defaultdict(list)
        
        for word in strs:
            temp_chars = [0] * 26
            for c in word:
                temp_chars[ord(c) - ord('a')] += 1
            result_map[tuple(temp_chars)].append(word)
        return list(result_map.values())