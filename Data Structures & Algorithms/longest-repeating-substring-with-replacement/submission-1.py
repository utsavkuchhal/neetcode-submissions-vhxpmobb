from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(lambda: 0)
        max_len, max_freq = 0, 0
        left, right = 0, 0
        while right < len(s):
            freq_map[s[right]] += 1
            max_freq = max(max_freq, freq_map[s[right]])
            while (right - left + 1 - max_freq) > k and left < right:
                freq_map[s[left]] -= 1
                max_freq = max(max_freq, freq_map[s[left]])
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
            