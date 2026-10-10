class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        max_diff = 0
        diffs = []
        for n1 , n2 in zip(nums1 , nums2):
            d = abs(n1 - n2)
            diffs.append(d)
            if d > max_diff:
                max_diff = d
        if max_diff == 0:
            return 0
        diff_count = [0]*(max_diff + 1)
        for d in diffs:
            diff_count[d] += 1
        for d in range(max_diff , 0 , -1):
            if diff_count[d] == 0:
                continue
            take = min(diff_count[d] , k)
            diff_count[d] -= take
            diff_count[d-1] += take
            k -= take
            if k == 0:
                break
        ans = 0
        for d in range(1,max_diff+1):
            if diff_count[d] > 0:
                ans += diff_count[d]*(d**2)
        return ans