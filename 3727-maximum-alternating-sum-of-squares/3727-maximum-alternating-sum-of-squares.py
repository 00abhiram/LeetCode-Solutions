class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        neg_count = len(nums) // 2
        return sum(nums[neg_count:]) - sum(nums[:neg_count])