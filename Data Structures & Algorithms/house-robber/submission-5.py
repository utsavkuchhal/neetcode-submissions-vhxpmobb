class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        prev1, prev2 = 0, 0
        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr
        return curr
        # def solve(start, nums, total):
            
        #     if start >= len(nums):
        #         return total
        #     return max(solve(start + 1, nums, total), solve(start + 2, nums, total + nums[start]))

        # return solve(0, nums, 0)