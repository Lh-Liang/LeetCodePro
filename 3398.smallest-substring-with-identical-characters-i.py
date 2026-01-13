#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        INF = 10**9

        def can(L: int) -> bool:
            # dp0[len], dp1[len] for len in [1..L]
            dp0 = [INF] * (L + 1)
            dp1 = [INF] * (L + 1)

            dp0[1] = 0 if s[0] == '0' else 1
            dp1[1] = 0 if s[0] == '1' else 1

            for i in range(1, n):
                flip0 = 0 if s[i] == '0' else 1
                flip1 = 0 if s[i] == '1' else 1

                best0 = min(dp0[1:])
                best1 = min(dp1[1:])

                new0 = [INF] * (L + 1)
                new1 = [INF] * (L + 1)

                # switch character -> run length becomes 1
                new0[1] = min(new0[1], best1 + flip0)
                new1[1] = min(new1[1], best0 + flip1)

                # extend same character run
                for length in range(1, L):
                    if dp0[length] < INF:
                        new0[length + 1] = min(new0[length + 1], dp0[length] + flip0)
                    if dp1[length] < INF:
                        new1[length + 1] = min(new1[length + 1], dp1[length] + flip1)

                dp0, dp1 = new0, new1

                # costs only increase, so we can early stop
                if min(min(dp0[1:]), min(dp1[1:])) > numOps:
                    return False

            return min(min(dp0[1:]), min(dp1[1:])) <= numOps

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
# @lc code=end
