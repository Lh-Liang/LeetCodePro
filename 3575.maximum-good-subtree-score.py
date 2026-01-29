#
# @lc app=leetcode id=3575 lang=python3
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
from typing import List

class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        n = len(vals)
        MOD = 10**9 + 7
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[par[i]].append(i)
        self.n = n
        self.vals = vals
        self.MOD = MOD
        self.children = children
        self.valids = [False] * n
        self.masks = [0] * n
        for i in range(n):
            self.valids[i], self.masks[i] = self._get_digits(vals[i])
        self.total = 0
        self._dfs(0)
        return self.total % MOD

    def _get_digits(self, val: int) -> tuple[bool, int]:
        cnt = [0] * 10
        s = str(val)
        for char in s:
            d = ord(char) - ord('0')
            cnt[d] += 1
            if cnt[d] > 1:
                return False, 0
        mask = 0
        for i in range(10):
            if cnt[i] > 0:
                mask |= (1 << i)
        return True, mask

    def _dfs(self, u: int) -> list[int]:
        N = 1 << 10
        comb = [-1] * N
        comb[0] = 0
        for v in self.children[u]:
            child_dp = self._dfs(v)
            new_comb = [-1] * N
            for m1 in range(N):
                if comb[m1] < 0:
                    continue
                s1 = comb[m1]
                for m2 in range(N):
                    if child_dp[m2] < 0:
                        continue
                    if (m1 & m2) == 0:
                        nm = m1 | m2
                        ns = s1 + child_dp[m2]
                        if new_comb[nm] < ns:
                            new_comb[nm] = ns
            comb = new_comb
        # compute max_score_u
        max_score_u = 0
        for m in range(N):
            if comb[m] >= 0:
                max_score_u = max(max_score_u, comb[m])
        if self.valids[u]:
            masku = self.masks[u]
            valu = self.vals[u]
            for m in range(N):
                if comb[m] >= 0 and (m & masku) == 0:
                    max_score_u = max(max_score_u, comb[m] + valu)
        self.total = (self.total + max_score_u) % self.MOD
        # build dp_u
        dp_u = [-1] * N
        dp_u[0] = 0
        for m in range(N):
            if comb[m] >= 0:
                dp_u[m] = comb[m]
        if self.valids[u]:
            masku = self.masks[u]
            valu = self.vals[u]
            for m in range(N):
                if comb[m] >= 0 and (m & masku) == 0:
                    nm = m | masku
                    ns = comb[m] + valu
                    if dp_u[nm] < ns:
                        dp_u[nm] = ns
        return dp_u
# @lc code=end