from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.final_result = set()
        self.prefix_map = defaultdict(lambda: 0)
        for i in range(len(nums)):
            self.twoSum(nums, i)
            self.prefix_map[nums[i]] = i
        return [list(result) for result in self.final_result]

    def twoSum(self, nums, curr_idx):
        target = 0 - nums[curr_idx]
        for index in range(curr_idx + 1, len(nums)):
            new_target = target - nums[index]
            if new_target in self.prefix_map:
                temp = [nums[curr_idx], nums[index], new_target]
                temp.sort()
                self.final_result.add(tuple(temp))
        