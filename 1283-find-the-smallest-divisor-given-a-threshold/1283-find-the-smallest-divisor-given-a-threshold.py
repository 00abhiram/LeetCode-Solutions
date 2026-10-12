import math
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def compute_sum(divisor : int) -> int:
            return sum((x + divisor - 1)//divisor for x in nums)
        low = 1
        high = max(nums)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if compute_sum(mid) <= threshold:
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        return ans