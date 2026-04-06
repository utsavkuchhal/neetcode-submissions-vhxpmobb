class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        ans = [0] * len(temperatures)
        for index, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                top_val, top_index = stack.pop()
                ans[top_index] = index - top_index
            stack.append((val, index))
        return ans