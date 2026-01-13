#
# @lc app=leetcode id=3563 lang=python3
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)

        def consecutive(a: str, b: str) -> bool:
            d = abs(ord(a) - ord(b))
            return d == 1 or d == 25  # circular adjacency (a-z)

        # empty[l][r] == can s[l..r] be fully removed
        empty = [[False] * n for _ in range(n)]

        # length 1 intervals cannot become empty; start from length 2
        for length in range(2, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                ok = False
                # l must be paired with some k
                for k in range(l + 1, r + 1):
                    if not consecutive(s[l], s[k]):
                        continue
                    left_empty = True if k == l + 1 else empty[l + 1][k - 1]
                    if not left_empty:
                        continue
                    right_empty = True if k == r else empty[k + 1][r]
                    if right_empty:
                        ok = True
                        break
                empty[l][r] = ok

        # dp[i] = lexicographically smallest string obtainable from s[i:]
        dp = [""] * (n + 1)
        dp[n] = ""

        for i in range(n - 1, -1, -1):
            best = s[i] + dp[i + 1]  # keep s[i]

            # try pairing i with k to delete s[i] and s[k]
            for k in range(i + 1, n):
                if not consecutive(s[i], s[k]):
                    continue
                mid_empty = True if k == i + 1 else empty[i + 1][k - 1]
                if not mid_empty:
                    continue
                cand = dp[k + 1]
                if cand < best:
                    best = cand

            dp[i] = best

        return dp[0]
# @lc code=end
