#
# @lc app=leetcode id=3640 lang=python3
#
# [3640] Trionic Array II
#

from typing import List

# @lc code=start
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        INF = float('inf')
        NEG_INF = float('-inf')
        
        # max_inc_end[i]: max sum strict inc len>=2 ending at i
        len_inc = [1] * n
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                len_inc[i] = len_inc[i - 1] + 1
        max_inc_end = [NEG_INF] * n
        min_for_end = [INF] * n
        for i in range(1, n):
            if len_inc[i] >= 2:
                if len_inc[i] == 2:
                    min_for_end[i] = prefix[i - 1]
                else:
                    min_for_end[i] = min(min_for_end[i - 1], prefix[i - 1])
                max_inc_end[i] = prefix[i + 1] - min_for_end[i]
        
        # len_forward[i]: max inc length starting at i
        len_forward = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                len_forward[i] = len_forward[i + 1] + 1
        
        # max_inc_start[i]: max sum strict inc len>=2 starting at i
        max_inc_start = [NEG_INF] * n
        for i in range(n - 1, -1, -1):
            if len_forward[i] >= 2:
                next_max = max_inc_start[i + 1] if i + 1 < n else NEG_INF
                cand1 = nums[i + 1]
                max_add = max(cand1, next_max)
                max_inc_start[i] = nums[i] + max_add
        
        # len_dec[i]: max dec length ending at i
        len_dec = [1] * n
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                len_dec[i] = len_dec[i - 1] + 1
        
        # B[p]
        B = [NEG_INF] * n
        for p in range(n):
            if max_inc_end[p] != NEG_INF:
                B[p] = max_inc_end[p] - prefix[p] - nums[p]
        
        # Now for each q
        ans = NEG_INF
        current_max_B = NEG_INF
        for q in range(n):
            if len_dec[q] >= 2:
                if len_dec[q] == 2:
                    current_max_B = B[q - 1]
                else:
                    current_max_B = max(current_max_B, B[q - 1])
                if current_max_B != NEG_INF and max_inc_start[q] != NEG_INF:
                    c_q = prefix[q + 1] + max_inc_start[q] - nums[q]
                    total = current_max_B + c_q
                    ans = max(ans, total)
        
        return int(ans)
# @lc code=end
