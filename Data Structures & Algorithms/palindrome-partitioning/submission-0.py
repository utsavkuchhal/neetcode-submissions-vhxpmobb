class Solution:
    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []
        def solve(s, curr):
            if not s:
                result.append(curr.copy())
                return

            for i in range(1, len(s) + 1):
                left_s = s[:i]
                right_s = s[i:]
                if self.is_palindrome(left_s):
                    curr.append(left_s)
                    solve(right_s, curr)
                    curr.pop()
        solve(s, [])
        return result