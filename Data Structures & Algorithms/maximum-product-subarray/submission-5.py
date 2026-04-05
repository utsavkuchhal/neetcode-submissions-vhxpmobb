class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = 1
        curr_max = 1
        n = len(nums)
        result = nums[0]
        for index in range(n):
            prev_max = curr_max
            prev_min = curr_min
            curr_max = max(nums[index], nums[index] * prev_max, nums[index] * prev_min)
            curr_min = min(nums[index], nums[index] * prev_max, nums[index] * prev_min)
            result = max(result, curr_max)
        return result
