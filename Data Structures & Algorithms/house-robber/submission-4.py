class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        prev1 = nums[0]
        prev2 = 0
        curr = nums[0]
        for index in range(2, n + 1):
            curr = max(prev1, prev2 + nums[index - 1])
            prev2 = prev1
            prev1 = curr
        return curr
        # def solve(start, nums, total):
            
        #     if start >= len(nums):
        #         return total
        #     return max(solve(start + 1, nums, total), solve(start + 2, nums, total + nums[start]))

        # return solve(0, nums, 0)