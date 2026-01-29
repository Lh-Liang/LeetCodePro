#
# @lc app=leetcode id=3544 lang=python3
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
import sys

class Solution:
    def subtreeInversionSum(self, edges: list[list[int]], nums: list[int], k: int) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Post-order traversal to process children before parents
        order = []
        stack = [0]
        parent = [-1] * n
        visited = [False] * n
        visited[0] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)
        
        # dp[u][d][p]: max sum of subtree u given dist d to nearest inv ancestor and parity p
        # We use a flat list or separate variables to optimize Python performance
        # dp_table[u] will store a list of size (k+1)*2
        dp = [None] * n

        for u in reversed(order):
            # Pre-calculate sums of children for all possible (next_d, next_p)
            # child_sums[d][p] = sum(dp[v][d][p] for v in children)
            child_sums = [0] * ((k + 1) * 2)
            for v in adj[u]:
                if v == parent[u]:
                    continue
                v_dp = dp[v]
                for i in range(len(v_dp)):
                    child_sums[i] += v_dp[i]

            u_dp = [0] * ((k + 1) * 2)
            for p in range(2):
                # Case: Invert at u (only if dist to ancestor >= k)
                # If we invert at u, the node value is flipped relative to parity p
                # and children see distance 1 and parity 1-p
                res_inv = ((-nums[u] if p == 0 else nums[u]) + 
                           child_sums[1 * 2 + (1 - p)])
                
                for d in range(1, k + 1):
                    # Case: Don't invert at u
                    next_d = min(k, d + 1)
                    res_no = (nums[u] if p == 0 else -nums[u]) + \
                             child_sums[next_d * 2 + p]
                    
                    if d >= k:
                        u_dp[d * 2 + p] = max(res_no, res_inv)
                    else:
                        u_dp[d * 2 + p] = res_no
            dp[u] = u_dp

        # Initial state: root has no inverted ancestors (dist k, parity 0)
        return dp[0][k * 2 + 0]
# @lc code=end