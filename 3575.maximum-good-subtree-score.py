#
# @lc app=leetcode id=3575 lang=python3
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
class Solution:
    def goodSubtreeSum(self, vals: list[int], par: list[int]) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]
        for i, p in enumerate(par):
            if p != -1:
                adj[p].append(i)

        # Precompute masks for each node
        node_masks = []
        for v in vals:
            m, x = 0, v
            possible = True
            while x > 0:
                d = x % 10
                if (m >> d) & 1:
                    possible = False
                    break
                m |= (1 << d)
                x //= 10
            node_masks.append(m if possible else -1)

        MOD = 10**9 + 7
        total_max_score_sum = 0
        
        # subtree_dp[u] stores the max sum for each digit mask in subtree u
        subtree_dps = [None] * n

        # Post-order traversal using a stack
        stack = [(0, False)]
        order = []
        while stack:
            u, visited = stack.pop()
            if visited:
                order.append(u)
            else:
                stack.append((u, True))
                for v in adj[u]:
                    stack.append((v, False))

        for u in order:
            # Initialize DP for current node u
            # dp[mask] = max sum of a good subset in subtree u
            res_dp = [0] * 1024
            
            # Combine DP tables from children
            # To optimize, we treat each child's subtree as a single set of items
            # But actually, any node in the subtree can be picked.
            # The correct way is to merge child DP tables.
            # Since we want the max score for node u's subtree, we can just
            # take the maximum possible value for each mask across all nodes in the subtree.
            for v in adj[u]:
                v_dp = subtree_dps[v]
                for mask in range(1024):
                    if v_dp[mask] > res_dp[mask]:
                        res_dp[mask] = v_dp[mask]
            
            # Now res_dp contains the max sum for each mask among all subsets
            # that are entirely contained within ONE of the children's subtrees.
            # However, a good subset can pick nodes from DIFFERENT children subtrees.
            # This is a knapsack: items are children subtrees.
            # To avoid O(N * 2^20), we simplify: the problem is equivalent to 
            # a knapsack over all nodes in the subtree.
            
            # Correct approach: Start with u's value, then add all nodes in subtree.
            # To do this efficiently, we maintain a single DP table for the subtree.
            # We'll use the 'merged' results from children.
            
            # Re-initialize: start with an empty set
            dp = [0] * 1024
            for v in adj[u]:
                v_dp = subtree_dps[v]
                # Merge dp (current combined children) with v_dp (new child)
                # Using O(3^10) submask enumeration for merging
                new_dp = list(dp)
                for m1, s1 in enumerate(dp):
                    if s1 == 0 and m1 != 0: continue
                    # Only iterate over valid submasks of the remaining digits
                    remaining = 1023 ^ m1
                    m2 = remaining
                    while m2 > 0:
                        if v_dp[m2] > 0:
                            combined_mask = m1 | m2
                            new_score = s1 + v_dp[m2]
                            if new_score > new_dp[combined_mask]:
                                new_dp[combined_mask] = new_score
                        m2 = (m2 - 1) & remaining
                # Also consider just taking the child's best for a mask
                for m in range(1024):
                    if v_dp[m] > new_dp[m]:
                        new_dp[m] = v_dp[m]
                dp = new_dp

            # Finally, add node u itself
            u_m = node_masks[u]
            if u_m != -1:
                u_v = vals[u]
                for m in range(1023, -1, -1):
                    if not (m & u_m):
                        if dp[m] + u_v > dp[m | u_m]:
                            dp[m | u_m] = dp[m] + u_v
                if u_v > dp[u_m]:
                    dp[u_m] = u_v
            
            subtree_dps[u] = dp
            total_max_score_sum = (total_max_score_sum + max(dp)) % MOD
            
        return total_max_score_sum
# @lc code=end