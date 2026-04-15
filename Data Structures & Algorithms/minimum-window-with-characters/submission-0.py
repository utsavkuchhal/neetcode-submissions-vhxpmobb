from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s2: str, s1: str) -> str:
        need = Counter(s1)
        need_count, have_count = len(need), 0
        have = defaultdict(lambda: 0)
        min_len = float('inf')
        left = 0
        result = [-1, -1]
        for right in range(len(s2)):
            char = s2[right]
            have[char] += 1
            if char in need and need[char] == have[char]:
                have_count += 1
            while have_count == need_count:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = [left, right]
                have[s2[left]] -= 1
                if s2[left] in need and have[s2[left]] < need[s2[left]]:
                    have_count -= 1
                left += 1
        return s2[result[0]: result[1] + 1] if min_len != float('inf') else ""