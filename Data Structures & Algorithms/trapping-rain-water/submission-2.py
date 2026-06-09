class Solution:
    def trap2(self, height):
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_curr_max = height[0]
        right_curr_max = height[n - 1]
        for i in range(1, n):
            left_curr_max = max(left_curr_max, height[i])
            left_max[i] = left_curr_max
        
        for i in range(n - 1, -1, -1):
            right_curr_max = max(right_curr_max, height[i])
            right_max[i] = right_curr_max
        
        ans = 0
        for i in range(n):
            sub = min(left_max[i], right_max[i]) - height[i]
            if sub > 0:
                ans += sub
        return ans
    
    def trap(self, height: List[int]) -> int:
        return self.trap2(height)
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left+=1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water