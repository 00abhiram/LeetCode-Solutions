class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_partition(max_sum: int) -> bool:
            current_sum = 0
            subarrays_count = 1
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays_count += 1
                    current_sum = num
                    if subarrays_count > k:
                        return False
                else:
                    current_sum += num
            return True
        low , high =  max(nums) , sum(nums)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can_partition(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans