class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        max_count, curr_count = 0, 0
        for val in arr:
            curr_count = 0
            while val in arr:
                val += 1
                curr_count += 1
            max_count = max(max_count, curr_count)
        return max_count
