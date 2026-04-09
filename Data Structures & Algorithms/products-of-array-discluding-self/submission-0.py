import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product, suffix_product = [1] * n, [1] * n
        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]
        result = []
        for i in range(0, n):
            result.append(prefix_product[i] *  suffix_product[i])
        return result

