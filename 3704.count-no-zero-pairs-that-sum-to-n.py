#
# @lc app=leetcode id=3704 lang=python3
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = str(n)
        self.L = len(s)
        self.dn = [int(c) for c in s]
        self.memo = {}
        return self.dfs(0, 0, 0, 0)

    def dfs(self, pos: int, delta: int, sa: int, sb: int) -> int:
        if pos == self.L:
            return 1 if delta == 0 and sa == 1 and sb == 1 else 0
        key = (pos, delta, sa, sb)
        if key in self.memo:
            return self.memo[key]
        ans = 0
        a_min = 1 if sa == 1 else 0
        b_min = 1 if sb == 1 else 0
        for da in range(a_min, 10):
            nsa = 1 if sa == 1 or da > 0 else 0
            for db in range(b_min, 10):
                nsb = 1 if sb == 1 or db > 0 else 0
                ndelta = self.dn[pos] - da - db + delta * 10
                if 0 <= ndelta <= 2:
                    ans += self.dfs(pos + 1, ndelta, nsa, nsb)
        self.memo[key] = ans
        return ans
# @lc code=end