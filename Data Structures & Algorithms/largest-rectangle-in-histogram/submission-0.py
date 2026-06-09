class Solution:
    def prev_small(self, arr):
        n = len(arr)
        prev_small = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            if stack:
                prev_small[i] = stack[-1]
            stack.append(i)
        return prev_small
    
    def next_small(self, arr):
        n = len(arr)
        stack = []
        next_small = [n] * n
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                next_small[stack.pop()] = i
            stack.append(i)
        return next_small
                

    def largestRectangleArea(self, heights: List[int]) -> int:
        next_small = self.next_small(heights)
        prev_small = self.prev_small(heights)
        max_area = 0
        for i in range(len(heights)):
            width = next_small[i] - prev_small[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        return max_area




