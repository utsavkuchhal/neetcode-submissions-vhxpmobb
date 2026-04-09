class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, ans, n = 0, 0, 0, len(s)
        char_set = set()
        while right < n:
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            ans = max(ans, right - left + 1)
            right += 1
        return ans
            