#
# @lc app=leetcode id=3575 lang=python3
#
# [3575] Maximum Good Subtree Score
#

from typing import List

# @lc code=start
class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(vals)

        # Build rooted tree children lists
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[par[i]].append(i)

        # Precompute digit masks; -1 means invalid (repeated digit within the number)
        def digit_mask(x: int) -> int:
            m = 0
            while x > 0:
                d = x % 10
                bit = 1 << d
                if m & bit:
                    return -1
                m |= bit
                x //= 10
            return m

        node_mask = [digit_mask(v) for v in vals]

        # Precompute submasks for every mask (total ~59049 entries)
        submasks = [[] for _ in range(1 << 10)]
        for S in range(1 << 10):
            t = S
            while True:
                submasks[S].append(t)
                if t == 0:
                    break
                t = (t - 1) & S

        NEG = -10**30  # safely below any achievable sum

        # Postorder traversal order
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in children[u]:
                stack.append(v)

        dp = [None] * n  # dp[u] is a list length 1024
        maxScoreSum = 0

        # Merge function using max-plus subset convolution
        def merge(a: List[int], b: List[int]) -> List[int]:
            new = [NEG] * 1024
            for S in range(1024):
                best = NEG
                for t in submasks[S]:
                    va = a[t]
                    if va == NEG:
                        continue
                    vb = b[S ^ t]
                    if vb == NEG:
                        continue
                    s = va + vb
                    if s > best:
                        best = s
                new[S] = best
            return new

        for u in reversed(order):
            cur = [NEG] * 1024
            cur[0] = 0

            for v in children[u]:
                cur = merge(cur, dp[v])

            m = node_mask[u]
            if m != -1:
                val_u = vals[u]
                for S in range(1024):
                    if cur[S] == NEG:
                        continue
                    if (S & m) == 0:
                        ns = S | m
                        cand = cur[S] + val_u
                        if cand > cur[ns]:
                            cur[ns] = cand

            dp[u] = cur
            max_u = max(cur)
            maxScoreSum = (maxScoreSum + max_u) % MOD

        return maxScoreSum
# @lc code=end
