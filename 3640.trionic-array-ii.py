#
# @lc app=leetcode id=3640 lang=python3
#
# [3640] Trionic Array II
#

# @lc code=start
from typing import List
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        NEG_INF = -10**18
        left_inc = [NEG_INF] * n
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                inner = nums[i - 1]
                if left_inc[i - 1] != NEG_INF:
                    inner = max(inner, left_inc[i - 1])
                left_inc[i] = nums[i] + inner
        right_inc = [NEG_INF] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inner = nums[i + 1]
                if right_inc[i + 1] != NEG_INF:
                    inner = max(inner, right_inc[i + 1])
                right_inc[i] = nums[i] + inner
        right_dec_end = list(range(n))
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                right_dec_end[i] = right_dec_end[i + 1]
            else:
                right_dec_end[i] = i
        left_sums = [NEG_INF] * n
        i = 0
        while i < n:
            s = i
            t = right_dec_end[s]
            if t > s:
                running_max = NEG_INF
                for q in range(s + 1, t + 1):
                    p = q - 1
                    if left_inc[p] != NEG_INF:
                        val = left_inc[p] - pre[p + 1]
                        running_max = max(running_max, val)
                    if running_max != NEG_INF:
                        left_sums[q] = pre[q + 1] + running_max
            i = t + 1
        ans = NEG_INF
        for q in range(n):
            if left_sums[q] != NEG_INF and right_inc[q] != NEG_INF:
                candidate = left_sums[q] + right_inc[q] - nums[q]
                if candidate > ans:
                    ans = candidate
        return ans

# @lc code=end