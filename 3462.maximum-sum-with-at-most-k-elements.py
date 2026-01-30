#
# @lc app=leetcode id=3462 lang=python3
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
from typing import List
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        dp = [0] + [-float('inf')] * k  # dp[x]: max sum picking x elements
        for row, limit in zip(grid, limits):
            row = sorted(row, reverse=True)
            prefix = [0]
            for i in range(min(limit, len(row))):
                prefix.append(prefix[-1] + row[i])
            ndp = dp[:]
            for cnt in range(1, len(prefix)):
                for x in range(k, cnt-1, -1):
                    if dp[x-cnt] != -float('inf'):
                        ndp[x] = max(ndp[x], dp[x-cnt] + prefix[cnt])
            dp = ndp
        # Verify at least one valid selection exists for 0 <= x <= k
        max_sum = max(dp)
        return max_sum if max_sum != -float('inf') else 0
# @lc code=end