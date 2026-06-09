from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        chars1, chars2 = [0] * 26, [0] * 26
        for char in s1:
            chars1[ord(char) - ord('a')] += 1

        for right in range(len(s1)):
            chars2[ord(s2[right]) - ord('a')] += 1

        if chars1 == chars2:
            return True
        left = 0
        right += 1
        while right < len(s2):
            chars2[ord(s2[right]) - ord('a')] += 1
            chars2[ord(s2[left]) - ord('a')] -= 1
            if chars1 == chars2:
                return True
            right += 1
            left += 1
        return False