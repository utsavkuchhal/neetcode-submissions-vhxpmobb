import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_map = dict()
        stack = list()
        for index, value in enumerate(position):
            speed_map[value] = speed[index]
        position.sort()
        for pos in position:
            time = (target - pos) / speed_map[pos]
            stack.append(time)
        head = stack[-1]
        count = 1
        while stack:
            if stack[-1] <= head:
                stack.pop()
            else:
                head = stack[-1]
                count +=1
        return count

