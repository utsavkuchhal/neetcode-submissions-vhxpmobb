class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            temp = 0
            while n:
                digit = n % 10
                n = n // 10
                temp += digit ** 2
            n = temp
            if temp == 1:
                return True
            if temp in visited:
                return False
            visited.add(temp)