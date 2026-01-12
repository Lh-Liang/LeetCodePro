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
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[par[i]].append(i)
        
        def get_mask(val):
            m = 0
            s = str(val)
            for char in s:
                digit = int(char)
                bit = 1 << digit
                if m & bit:
                    return -1
                m |= bit
            return m

        val_masks = [get_mask(v) for v in vals]
        MOD = 10**9 + 7
        total_max_score_sum = 0

        # We need to compute DP for each node's subtree
        # dp[u] will be a dictionary {mask: max_sum}
        def solve(u):
            nonlocal total_max_score_sum
            # current_dp represents the max sum for each mask in the subtree of u
            current_dp = {0: 0}
            
            # Process children
            for v in adj[u]:
                child_dp = solve(v)
                new_dp = current_dp.copy()
                for m1, s1 in current_dp.items():
                    for m2, s2 in child_dp.items():
                        if m2 == 0: continue
                        if (m1 & m2) == 0:
                            combined_mask = m1 | m2
                            new_score = s1 + s2
                            if new_score > new_dp.get(combined_mask, -1):
                                new_dp[combined_mask] = new_score
                current_dp = new_dp
            
            # After combining all children, we have the max sums for subsets NOT including u.
            # Now consider subsets including u.
            u_mask = val_masks[u]
            if u_mask != -1:
                # To include u, we must combine it with a mask from the children
                # that doesn't conflict with u_mask.
                # However, the problem says "a subset of nodes within the subtree".
                # This means we can pick any nodes such that digits are unique.
                # The logic above already finds the best subset within the subtree
                # formed by children. Now we just need to try adding u.
                for m, s in list(current_dp.items()):
                    if (m & u_mask) == 0:
                        new_mask = m | u_mask
                        new_score = s + vals[u]
                        if new_score > current_dp.get(new_mask, -1):
                            current_dp[new_mask] = new_score
            
            max_val = max(current_dp.values()) if current_dp else 0
            total_max_score_sum = (total_max_score_sum + max_val) % MOD
            return current_dp

        solve(0)
        return total_max_score_sum

# @lc code=end