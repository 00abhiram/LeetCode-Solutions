class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.sum_sq = [0] * (4 * n)
        self.sum_val = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push(self, node, start, end):
        if self.lazy[node] == 0:
            return
        
        val = self.lazy[node]
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1
        len_l = mid - start + 1
        self.sum_sq[left_child] = (self.sum_sq[left_child] + 2 * val * self.sum_val[left_child] + len_l * val * val) % self.MOD
        self.sum_val[left_child] = (self.sum_val[left_child] + len_l * val) % self.MOD
        self.lazy[left_child] = (self.lazy[left_child] + val) % self.MOD
        len_r = end - mid
        self.sum_sq[right_child] = (self.sum_sq[right_child] + 2 * val * self.sum_val[right_child] + len_r * val * val) % self.MOD
        self.sum_val[right_child] = (self.sum_val[right_child] + len_r * val) % self.MOD
        self.lazy[right_child] = (self.lazy[right_child] + val) % self.MOD
        
        self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            length = end - start + 1
            self.sum_sq[node] = (self.sum_sq[node] + 2 * val * self.sum_val[node] + length * val * val) % self.MOD
            self.sum_val[node] = (self.sum_val[node] + length * val) % self.MOD
            self.lazy[node] = (self.lazy[node] + val) % self.MOD
            return
        
        self._push(node, start, end)
        mid = (start + end) // 2
        if l <= mid:
            self.update(2 * node, start, mid, l, r, val)
        if r > mid:
            self.update(2 * node + 1, mid + 1, end, l, r, val)
        self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % self.MOD
        self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % self.MOD
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        tree = SegmentTree(n)
            
        last_pos = {}
        total_ans = 0
        
        for j, num in enumerate(nums):
            last_idx = last_pos.get(num, -1)
            tree.update(1, 0, n - 1, last_idx + 1, j, 1)
            total_ans = (total_ans + tree.sum_sq[1]) % MOD
            last_pos[num] = j
        return total_ans
