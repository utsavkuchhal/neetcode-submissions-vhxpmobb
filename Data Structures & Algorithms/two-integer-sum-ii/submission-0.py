class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            curr_sum = numbers[start] + numbers[end]
            if curr_sum == target:
                return [start + 1, end + 1]
            if curr_sum < target:
                start += 1
            else:
                end -= 1
        return -1
