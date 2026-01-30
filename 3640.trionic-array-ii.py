# @lc app=leetcode id=3640 lang=python3
#
# [3640] Trionic Array II
#
from typing import List

# @lc code=start
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
        
        # Auxiliary arrays for tracking maximum sums of increasing sequences
        left_increase = [0] * n
        right_increase = [0] * n
        
        # Initialize left_increase array by iterating from left to right
        left_sum = nums[0]
        left_increase[0] = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left_sum += nums[i]
            else:
                left_sum = nums[i]
            left_increase[i] = max(left_increase[i - 1], left_sum)
        
        # Initialize right_increase array by iterating from right to left
        right_sum = nums[-1]
        right_increase[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right_sum += nums[i]
            else:
                right_sum = nums[i]
            right_increase[i] = max(right_increase[i + 1], right_sum)
        
        # Track maximum trionic sum found
        max_trionic_sum = float('-inf')

        # Check each potential peak point for middle decreasing sequences and calculate total sum
        for p in range(1, n - 2):
            if nums[p - 1] < nums[p] > nums[p + 1]:
                middle_sum = nums[p]
                q = p + 1
                # Extend middle decrease as far as valid
                while q < n - 1 and nums[q] > nums[q + 1]:
                    middle_sum += nums[q]
                    q += 1
                # If valid sequence found, calculate total trionic sum using precomputed values
                if q < n - 1 and q > p + 1:
                    total_sum = left_increase[p - 1] + middle_sum + right_increase[q]b max_trionic_sum = max(max_trionic_sum, total_sum)b b return max_trionic_sumb # @lc code=end