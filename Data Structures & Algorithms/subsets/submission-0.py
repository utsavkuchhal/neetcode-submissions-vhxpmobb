import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def solve(index, curr_set):
            if index == n:
                temp = curr_set.copy()
                result.append(temp)
                return
                
            solve(index + 1, curr_set)
            curr_set.append(nums[index])
            solve(index + 1, curr_set)
            curr_set.pop()
        solve(0, [])
        return result

                