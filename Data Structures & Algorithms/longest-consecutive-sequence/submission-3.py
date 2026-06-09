class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        max_count, curr_count = 0, 0
        for val in nums:
            if val - 1 not in arr:
                curr_count = 0
                while val in arr:
                    curr_count += 1
                    val += 1
                max_count = max(curr_count, max_count)
        return max_count