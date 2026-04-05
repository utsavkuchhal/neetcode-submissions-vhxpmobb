class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def count(start, end):
            while start >= 0 and end < n and s[start] == s[end]:
                nonlocal res
                res += 1
                start -= 1
                end += 1

        n = len(s)
        for index in range(n):
            count(index, index)
            count(index, index + 1)
        return res
