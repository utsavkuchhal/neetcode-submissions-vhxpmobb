class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for index in range(2, n + 1):
            dp[index] = max(dp[index - 1], dp[index - 2] + nums[index - 1])
        return dp[n]
        
        # def solve(start, nums, total):
            
        #     if start >= len(nums):
        #         return total
        #     return max(solve(start + 1, nums, total), solve(start + 2, nums, total + nums[start]))

        # return solve(0, nums, 0)