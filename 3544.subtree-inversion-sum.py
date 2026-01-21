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
    def subtreeInversionSum(self, edges: list[list[int]], nums: list[int], k: int) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # dp[u][i] where i in [0, k-1] means parity 0, nearest flip at dist i (0 = none)
        # dp[u][i+k] where i in [0, k-1] means parity 1, nearest flip at dist i (0 = none)
        # Note: 'none' is distance infinity, but we use 0 to represent 'available to flip'
        
        memo = {}

        # Flatten tree to process iteratively or use optimized recursion
        order = []
        parent = [-1] * n
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    stack.append(v)
        
        # dp[u][state] 
        # state 0: parity 0, can flip (no flipped ancestor within k-1)
        # state 1..k-1: parity 0, nearest flipped ancestor at distance state
        # state k: parity 1, can flip (no flipped ancestor within k-1) - Impossible state by logic but kept for indexing
        # state k..2k-1: parity 1, nearest flipped ancestor at distance state-k
        
        dp = [[0] * (2 * k) for _ in range(n)]

        for u in reversed(order):
            for state in range(2 * k):
                p = state // k
                dist = state % k
                
                val = nums[u] if p == 0 else -nums[u]
                
                # Option 1: Don't flip u
                res_no_flip = val
                next_dist = 0 if dist == 0 or dist + 1 >= k else dist + 1
                next_state = p * k + next_dist
                for v in adj[u]:
                    if v != parent[u]:
                        res_no_flip += dp[v][next_state]
                
                # Option 2: Flip u (only if dist == 0)
                if dist == 0:
                    res_flip = -val
                    next_state_flip = (1 - p) * k + 1
                    for v in adj[u]:
                        if v != parent[u]:
                            res_flip += dp[v][next_state_flip]
                    dp[u][state] = max(res_no_flip, res_flip)
                else:
                    dp[u][state] = res_no_flip

        return dp[0][0]
# @lc code=end