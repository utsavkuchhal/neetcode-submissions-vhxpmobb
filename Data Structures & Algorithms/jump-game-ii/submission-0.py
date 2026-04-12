class Solution:
    def jump(self, nums: List[int]) -> int:
        can_reach = [float('inf')] * len(nums)
        can_reach[0] = 0
        for index, num in enumerate(nums):
            prev = can_reach[index]
            i = index + 1
            while i <= index + num and i < len(nums):
                can_reach[i] = min(prev + 1, can_reach[i])
                i += 1
        return can_reach[-1]