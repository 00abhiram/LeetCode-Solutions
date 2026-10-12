class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            current_days = 1
            current_weight = 0
            for w in weights:
                if current_weight + w > capacity:
                    current_days += 1
                    current_weight = w
                else:
                    current_weight += w
            return current_days <= days
        left = max(weights)
        right = sum(weights)
        while left<right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid 
            else:
                left = mid + 1
        return left