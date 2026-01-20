#
# @lc app=leetcode id=3670 lang=python3
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

from typing import List

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        B = 20
        ALL = (1 << B) - 1
        dp = [0] * (1 << B)
        for num in nums:
            dp[num] = max(dp[num], num)
        for bit in range(B):
            for mask in range(1 << B):
                if (mask & (1 << bit)) == 0:
                    on_mask = mask | (1 << bit)
                    dp[on_mask] = max(dp[on_mask], dp[mask])
        ans = 0
        for mask in range(1 << B):
            comp = ALL ^ mask
            ans = max(ans, dp[mask] * dp[comp])
        return ans
# @lc code=end
