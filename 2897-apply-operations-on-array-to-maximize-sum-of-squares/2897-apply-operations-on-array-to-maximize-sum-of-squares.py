class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Count the frequency of 1s at each bit position (up to 30 bits for nums[i] <= 10^9)
        bit_counts = [0] * 30
        for num in nums:
            for i in range(30):
                if (num >> i) & 1:
                    bit_counts[i] += 1
        
        total_sum_squares = 0
        
        # Greedily form the k largest possible numbers
        for _ in range(k):
            current_num = 0
            for i in range(30):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            
            # Add the square of the current number to the answer
            total_sum_squares = (total_sum_squares + current_num * current_num) % MOD
            
        return total_sum_squares
