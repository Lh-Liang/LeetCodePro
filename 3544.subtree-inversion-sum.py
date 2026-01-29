#
# @lc app=leetcode id=3544 lang=python3
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Iterative post-order traversal
        order = []
        stack = [0]
        parent = [-1] * n
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    stack.append(v)
        
        # dp[u] stores two lists: [dp_u_parity0, dp_u_parity1]
        # each list is of size k+1 representing distance d
        dp = [None] * n
        
        for u in reversed(order):
            # Pre-calculate sums from children for both parities
            # s0[d] is sum of dp[v][0][d], s1[d] is sum of dp[v][1][d]
            s0 = [0] * (k + 1)
            s1 = [0] * (k + 1)
            for v in adj[u]:
                if v == parent[u]: continue
                v_dp0, v_dp1 = dp[v]
                for d in range(1, k + 1):
                    s0[d] += v_dp0[d]
                    s1[d] += v_dp1[d]
            
            dp_u_0 = [0] * (k + 1)
            dp_u_1 = [0] * (k + 1)
            val = nums[u]
            
            # Distance d < k: Inversion not allowed
            for d in range(1, k):
                dp_u_0[d] = val + s0[min(k, d + 1)]
                dp_u_1[d] = -val + s1[min(k, d + 1)]
            
            # Distance d = k: Can choose to invert or not
            # Parity 0: Max(Not Invert [val + s0[k]], Invert [-val + s1[1]])
            dp_u_0[k] = max(val + s0[k], -val + s1[1])
            # Parity 1: Max(Not Invert [-val + s1[k]], Invert [val + s0[1]])
            dp_u_1[k] = max(-val + s1[k], val + s0[1])
            
            dp[u] = (dp_u_0, dp_u_1)
            
        return dp[0][0][k]
# @lc code=end