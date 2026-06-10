class Solution:
    # 3, 4, 5, 1, 2
    # left = 0, right = 1 mid = 0 nums[mid] = 2
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_val = float('inf')
        while left <= right:
            if nums[left] <= nums[right]:
                min_val = min(min_val, nums[left])
                break
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                min_val = min(min_val, nums[left])
                left = mid + 1
            else:
                min_val = min(min_val, nums[mid])
                right = mid - 1
        return min_val

        