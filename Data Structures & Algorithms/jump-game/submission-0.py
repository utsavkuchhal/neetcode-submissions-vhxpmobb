class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False] * len(nums)
        can_reach[0] = True
        for index, num in enumerate(nums):
            if can_reach[index] != True:
                break
            i = index + 1
            while i <= index + num and i < len(nums):
                can_reach[i] = True
                i += 1
        return can_reach[-1]



