class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(nums):
            n = len(nums)
            dp = [0] * (n + 1)
            dp[1] = nums[0]
            for index in range(2, n + 1):
                dp[index] = max(dp[index - 1], dp[index - 2] + nums[index - 1])
            return dp[n]
        if len(nums) == 1:
            return nums[0]
        return max(solve(nums[1:]), solve(nums[:-1]))