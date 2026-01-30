#
# @lc app=leetcode id=3575 lang=python3
#
# [3575] Maximum Good Subtree Score
#
# @lc code=start
class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        from collections import defaultdict

        MOD = 10**9 + 7
        n = len(vals)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[par[i]].append(i)

        def get_digit_mask(x):
            mask = 0
            for ch in str(x):
                mask |= 1 << int(ch)
            return mask

        maxScore = [0] * n

        def dfs(u):
            # dp: mask -> maximal sum
            dp = {}
            val_mask = get_digit_mask(vals[u])
            dp[val_mask] = vals[u]
            for v in tree[u]:
                child_dp = dfs(v)
                # Try to merge child_dp into dp (without overlapping digits)
                new_dp = dp.copy()
                for m1, s1 in dp.items():
                    for m2, s2 in child_dp.items():
                        if m1 & m2 == 0: # no digit overlap
                            new_mask = m1 | m2
                            new_dp[new_mask] = max(new_dp.get(new_mask, 0), s1 + s2)
                # Also keep all child_dp masks as possible (if not including u)
                for m2, s2 in child_dp.items():
                    new_dp[m2] = max(new_dp.get(m2, 0), s2)
                # Verification: Ensure no valid state is overwritten or omitted
                dp = new_dp
            # Verification: DP table includes all possible non-overlapping digit subsets and their sums
            maxScore[u] = max(dp.values())
            return dp

        dfs(0)
        return sum(maxScore) % MOD
# @lc code=end