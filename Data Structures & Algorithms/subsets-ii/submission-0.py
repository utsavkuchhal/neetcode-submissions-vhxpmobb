class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        def solve(nums, index, subset):
            if index == len(nums):
                result.add(tuple(subset.copy()))
                return
            
            solve(nums, index + 1, subset)
            subset.append(nums[index])
            solve(nums, index + 1, subset)
            subset.pop()

        solve(nums, 0, [])

        return [list(arr) for arr in result]