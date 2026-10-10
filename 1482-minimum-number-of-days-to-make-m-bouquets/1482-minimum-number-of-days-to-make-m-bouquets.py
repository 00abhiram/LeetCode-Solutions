class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        def canMake(days: int) -> bool:
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m:
                    return True
            return False
        low =  min(bloomDay)
        high = max(bloomDay)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if canMake(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans