#
# @lc app=leetcode id=3544 lang=python3
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(10**6)

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # dp[u][d][p]: max sum in subtree u given:
        # d: distance from u to nearest inverted ancestor (1 to k, where k means >= k)
        # p: parity of inversions from root to u's parent (0 or 1)
        # Using a flat list for performance in Python
        memo = {}

        # Build tree structure to avoid parent issues in DFS
        tree = [[] for _ in range(n)]
        stack = [0]
        visited = [False] * n
        visited[0] = True
        order = []
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    tree[u].append(v)
                    stack.append(v)

        # DP state: dp[u][d][p]
        # We iterate backwards through the BFS/DFS order to compute DP bottom-up
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]

        for u in reversed(order):
            for d in range(1, k + 1):
                for p in range(2):
                    # Option 1: Don't invert u
                    val_no = nums[u] if p == 0 else -nums[u]
                    next_d = min(k, d + 1)
                    for v in tree[u]:
                        val_no += dp[v][next_d][p]
                    
                    # Option 2: Invert u (only if d == k)
                    if d == k:
                        val_inv = nums[u] if (1 - p) == 0 else -nums[u]
                        for v in tree[u]:
                            val_inv += dp[v][1][1 - p]
                        dp[u][d][p] = max(val_no, val_inv)
                    else:
                        dp[u][d][p] = val_no

        # Result is max sum starting at root with no inverted ancestors within k distance
        return dp[0][k][0]
# @lc code=end