#
# @lc app=leetcode id=3544 lang=python3
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
from typing import List, DefaultDict
from collections import defaultdict

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        import sys
        sys.setrecursionlimit(max(100000, n+10))

        # dp[u][d]: max sum of subtree rooted at u, where d is distance to last inversion above
        # d = 0 means last inversion was just at parent.
        # d >= k => inversion allowed at this node
        def dfs(u, par):
            # dp[d]: for d = 0..k, max sum of this subtree with distance d to last inversion above
            dp = [0] * (k+1)
            # Initialize:
            # Option 1: Do NOT invert at u
            # Option 2: Invert at u (if allowed)
            # For children, we need their dp tables
            children = [v for v in tree[u] if v != par]
            # First, get children's dp
            child_dp = [dfs(v, u) for v in children]

            # Option 1: do NOT invert at u
            # If d < k, we cannot invert at this node
            # For each d = 0..k-1:
            for d in range(k):
                total = nums[u]
                for cidx, v in enumerate(children):
                    total += child_dp[cidx][min(d+1, k)]
                dp[d] = total
            # Option 2: invert at u (only if d >= k)
            # When we invert at u, all values in subtree flipped
            # For d=k, inversion is allowed
            total = -nums[u]
            for cidx, v in enumerate(children):
                total += child_dp[cidx][1]  # after invert at u, distance to inversion above is 1
            if k >= 1:
                dp[k] = max(dp[k], total)
            # Also, for d >= k, inversion is allowed
            for d in range(k, k+1):
                # Option: invert at u
                total = -nums[u]
                for cidx, v in enumerate(children):
                    total += child_dp[cidx][1]
                dp[d] = max(dp[d], total)
            return dp

        res_dp = dfs(0, -1)
        return max(res_dp)
# @lc code=end