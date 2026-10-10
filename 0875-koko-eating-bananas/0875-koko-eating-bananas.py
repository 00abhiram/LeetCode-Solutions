import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left , right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            total_hours = sum(math.ceil(pile/mid) for pile in piles)
            if total_hours <= h:
                right = mid
            else:
                left = mid + 1
        return left