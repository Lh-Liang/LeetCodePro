#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
from collections import deque

class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        pref1 = [0] * (n + 1)
        for i, ch in enumerate(s, 1):
            pref1[i] = pref1[i - 1] + (ch == '1')

        INF = 10**18

        def feasible(L: int) -> bool:
            dp0 = [INF] * (n + 1)  # end with 0-block
            dp1 = [INF] * (n + 1)  # end with 1-block
            dp0[0] = dp1[0] = 0

            # dq1 keeps candidates for min(dp1[j] - pref1[j]) in current window
            # dq0 keeps candidates for min(dp0[j] - pref0[j]) in current window
            dq1 = deque([(0, 0)])  # (idx, value)
            dq0 = deque([(0, 0)])

            for i in range(1, n + 1):
                left = i - L

                while dq1 and dq1[0][0] < left:
                    dq1.popleft()
                while dq0 and dq0[0][0] < left:
                    dq0.popleft()

                ones_i = pref1[i]
                zeros_i = i - ones_i

                dp0[i] = ones_i + dq1[0][1]
                dp1[i] = zeros_i + dq0[0][1]

                v1 = dp1[i] - ones_i
                while dq1 and dq1[-1][1] >= v1:
                    dq1.pop()
                dq1.append((i, v1))

                v0 = dp0[i] - zeros_i
                while dq0 and dq0[-1][1] >= v0:
                    dq0.pop()
                dq0.append((i, v0))

            return min(dp0[n], dp1[n]) <= numOps

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
# @lc code=end
