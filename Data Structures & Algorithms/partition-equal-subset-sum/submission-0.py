class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        return self.target_sum(target, nums)

    def target_sum(self, target, nums):
        n = len(nums) + 1
        dp = [[False] * n for _ in range(target + 1)]

        dp[0][0] = True
    
        for i in range(1, target + 1):
            for j in range(1, n):
                dp[i][j] |= dp[i][j - 1]
                if nums[j - 1] <= i:
                    dp[i][j] |= dp[i - nums[j - 1]][j - 1]
        return dp[target][n - 1]