class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # P + N = total
        # P - N = target
        if total < abs(target) or (target + total) % 2 != 0:
            return 0
        fin_sum = (target + total) // 2 + 1
        n = len(nums) + 1
        dp = [[0] * fin_sum for i in range(n)]
        dp[0][0] = 1
        for row in range(1, n):
            for col in range(0, fin_sum):
                dp[row][col] = dp[row - 1][col]
                if nums[row - 1] <= col:
                    dp[row][col] += dp[row - 1][col - nums[row - 1]]
        return dp[n - 1][fin_sum - 1]


#       return 
# 
# if curr_sum == target and index == len(nums):
#   return 1
# add = solve(nums, index + 1, target, curr_sum - nums[i])
# sub = solve(nums, index + 1, target, curr_sum + nums[i])
# return add + sub
# 
# 
# 
# 
# 
# 
# 
# 

