#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start

from typing import List
from collections import deque

class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        def can_achieve(max_len: int) -> bool:
            if max_len == 0:
                return False
            pre = [[0] * (n + 1) for _ in range(2)]
            for i in range(n):
                pre[0][i + 1] = pre[0][i] + (1 if s[i] == '0' else 0)
                pre[1][i + 1] = pre[1][i] + (1 if s[i] == '1' else 0)
            INF = n + 1
            dp = [[INF] * 2 for _ in range(n + 1)]
            dp[0][0] = dp[0][1] = 0
            dqs = [deque(), deque()]
            # Initialize with j=0
            for c in range(2):
                dqs[c].append(0)
            for i in range(1, n + 1):
                for c in range(2):
                    opp = 1 - c
                    # Remove out-of-window
                    while dqs[c] and dqs[c][0] < i - max_len:
                        dqs[c].popleft()
                    min_g = INF
                    if dqs[c]:
                        j = dqs[c][0]
                        min_g = pre[c][j] - j + dp[j][opp]
                    if min_g != INF:
                        dp[i][c] = i - pre[c][i] + min_g
                # Now add i to both deques
                for c in range(2):
                    opp = 1 - c
                    g = pre[c][i] - i + dp[i][opp]
                    # Remove from back worse
                    while dqs[c] and (pre[c][dqs[c][-1]] - dqs[c][-1] + dp[dqs[c][-1]][opp]) >= g:
                        dqs[c].pop()
                    dqs[c].append(i)
            return min(dp[n][0], dp[n][1]) <= numOps
        
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if can_achieve(mid):
                right = mid
            else:
                left = mid + 1
        return left

# @lc code=end