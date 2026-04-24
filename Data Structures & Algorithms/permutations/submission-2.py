class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def solve(nums, visited, curr):
            if len(curr) == len(nums):
                result.append(curr.copy())
            for i in range(len(visited)):
                if visited[i] == False:
                    visited[i] = True
                    curr.append(nums[i])
                    solve(nums, visited, curr)
                    curr.pop()
                    visited[i] = False
        visited = [False] * len(nums)
        solve(nums, visited, [])
        return result
            