class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        left, right = 0, len(nums1)
        elements_in_left = (n + m + 1) // 2

        while left <= right:
            mid1 = (left + right) // 2
            mid2 = elements_in_left - mid1
            r1 = nums1[mid1] if mid1 < n else float('inf')
            r2 = nums2[mid2] if mid2 < m else float('inf')
            l1 = nums1[mid1 - 1] if mid1 - 1 >= 0 else float('-inf')
            l2 = nums2[mid2 - 1] if mid2 - 1 >= 0 else float('-inf')
            if l1 <= r2 and l2 <= r1:
                if (n + m) %  2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                right = mid1 - 1
            else:
                left = mid1 + 1
        return 0



