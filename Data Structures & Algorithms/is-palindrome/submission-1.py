class Solution:
    def clean_string(self, s):
        s = ''.join([c for c in s if c.isalnum()])
        return s.lower()

    def isPalindrome(self, s: str) -> bool:
        s = self.clean_string(s)
        print(s)
        left, right = 0, len(s) - 1
        while(left < right):
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
