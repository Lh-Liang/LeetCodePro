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
        NEG = -10**30  # safely below minimal possible sum (~ -1e14)

        dp1 = NEG  # inc, len>=2
        dp2 = NEG  # inc->dec, in dec phase, both parts len>=2
        dp3 = NEG  # inc->dec->inc, in final inc phase, all parts len>=2
        ans = NEG

        for i in range(1, n):
            a, b = nums[i - 1], nums[i]

            new_dp1 = NEG
            new_dp2 = NEG
            new_dp3 = NEG

            if a < b:
                # increasing edge
                new_dp1 = max(dp1 + b, a + b)
                new_dp3 = max(dp3 + b, dp2 + b)
            elif a > b:
                # decreasing edge
                new_dp2 = max(dp2 + b, dp1 + b)

            dp1, dp2, dp3 = new_dp1, new_dp2, new_dp3
            if dp3 > ans:
                ans = dp3

        return ans
# @lc code=end
