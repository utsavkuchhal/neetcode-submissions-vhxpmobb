class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        final_ans = 1
        n = len(nums) + 1 
        dp = [1] * n
        for i in range(2, n):
            for j in range(1, i):
                if nums[j - 1] < nums[i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    final_ans = max(final_ans, dp[i])
        return final_ans