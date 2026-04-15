class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = [0] * 26
        for i in range(len(s)):
            chars[ord(s[i]) - ord('a')] += 1
            chars[ord(t[i]) - ord('a')] -= 1
        return all([val == 0 for val in chars])
        