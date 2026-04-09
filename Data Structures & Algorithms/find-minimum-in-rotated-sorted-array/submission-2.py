class Solution:
    # 3, 4, 5, 1, 2
    # left = 0, right = 1 mid = 0 nums[mid] = 2
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
    
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        