class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(left, right):
            if left + 1 == right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
    
            max_coins = 0
            for i in range(left + 1, right):
                coins = (
                    dfs(left, i) +
                    dfs(i, right) + 
                    nums[left] * nums[i] * nums[right]
                )
                max_coins = max(max_coins, coins)
                dp[(left, right)] = max_coins
            return max_coins
        return dfs(0, len(nums) - 1)