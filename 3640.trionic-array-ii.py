#
# @lc app=leetcode id=3640 lang=python3
#
# [3640] Trionic Array II
#

# @lc code=start
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        # Precompute strictly increasing subarrays ending at i
        inc_left = [1]*n
        inc_sum_left = [nums[i] for i in range(n)]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc_left[i] = inc_left[i-1] + 1
                inc_sum_left[i] = inc_sum_left[i-1] + nums[i]
        # Precompute strictly increasing subarrays starting at i
        inc_right = [1]*n
        inc_sum_right = [nums[i] for i in range(n)]
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                inc_right[i] = inc_right[i+1] + 1
                inc_sum_right[i] = inc_sum_right[i+1] + nums[i]
        # Precompute strictly decreasing subarrays ending at i
        dec_left = [1]*n
        dec_sum_left = [nums[i] for i in range(n)]
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                dec_left[i] = dec_left[i-1] + 1
                dec_sum_left[i] = dec_sum_left[i-1] + nums[i]
        # Precompute strictly decreasing subarrays starting at i
        dec_right = [1]*n
        dec_sum_right = [nums[i] for i in range(n)]
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                dec_right[i] = dec_right[i+1] + 1
                dec_sum_right[i] = dec_sum_right[i+1] + nums[i]

        max_sum = float('-inf')
        # For every possible 'decrease' segment [p, q]
        # We want to find l < p < q < r
        for mid_start in range(1, n-2):
            # mid_start: possible p
            # mid_end: possible q
            for mid_end in range(mid_start+1, n-1):
                # Check if nums[mid_start:mid_end+1] is strictly decreasing
                if dec_left[mid_end] >= mid_end - mid_start + 1:
                    # Left inc: must end at mid_start-1, strictly increasing
                    left_len = inc_left[mid_start-1] if mid_start-1 >= 0 else 0
                    if left_len >= 1:
                        l = mid_start - left_len
                        left_sum = sum(nums[l:mid_start])
                    else:
                        continue
                    # Right inc: must start at mid_end+1, strictly increasing
                    right_len = inc_right[mid_end+1] if mid_end+1 < n else 0
                    if right_len >= 1:
                        r = mid_end + 1 + right_len - 1
                        right_sum = sum(nums[mid_end+1:r+1])
                    else:
                        continue
                    mid_sum = sum(nums[mid_start:mid_end+1])
                    total = left_sum + mid_sum + right_sum
                    max_sum = max(max_sum, total)
        return max_sum
# @lc code=end