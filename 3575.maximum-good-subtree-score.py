#
# @lc app=leetcode id=3575 lang=python3
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
from typing import List
class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(vals)

        # Build tree
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[par[i]].append(i)

        # Precompute digit masks for each value
        def get_digit_mask(x):
            mask = 0
            for d in str(x):
                bit = 1 << int(d)
                if mask & bit:
                    return -1  # duplicate digit in this value
                mask |= bit
            return mask

        digit_masks = [get_digit_mask(v) for v in vals]

        maxScore = [0] * n

        def dfs(u):
            table = {}  # mask -> max sum
            m = digit_masks[u]
            if m == -1:
                # If duplicate digits in value, can only take individually
                table = {}
            else:
                table[m] = vals[u]
            # Process children
            for v in tree[u]:
                child_table = dfs(v)
                new_table = dict(table)
                # Merge: for each mask in table and child_table, combine if no overlap
                for mask1, sum1 in table.items():
                    for mask2, sum2 in child_table.items():
                        if mask1 & mask2 == 0:
                            new_mask = mask1 | mask2
                            new_table[new_mask] = max(new_table.get(new_mask, 0), sum1 + sum2)
                # Also, bring over all child_table entries (subsets that don't include u)
                for mask2, sum2 in child_table.items():
                    new_table[mask2] = max(new_table.get(mask2, 0), sum2)
                table = new_table
            maxScore[u] = max(table.values()) if table else 0
            return table

        dfs(0)
        return sum(maxScore) % MOD
# @lc code=end