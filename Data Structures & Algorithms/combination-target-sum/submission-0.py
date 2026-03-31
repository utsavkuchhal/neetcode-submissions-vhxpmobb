class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final_solution = []
        def solve(nums, target, index, curr):
            if target == 0:
                final_solution.append(list(curr))
                return

            if target < 0 or index >= len(nums):
                return

            solve(nums, target, index + 1, curr)
            curr.append(nums[index])
            solve(nums, target - nums[index], index, curr)
            curr.pop()
        solve(nums, target, 0, [])
        return final_solution