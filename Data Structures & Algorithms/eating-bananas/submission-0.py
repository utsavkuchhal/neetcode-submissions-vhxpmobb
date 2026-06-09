import math
class Solution:
    def check_possible(self, piles, speed, h):
        total = 0
        for pile in piles:
            total += math.ceil(pile / speed)
        if total <= h:
            return True
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        if h < len(piles):
            return -1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            is_possible = self.check_possible(piles, mid, h)
            print(mid, is_possible)
            if is_possible:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
            
