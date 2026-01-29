#
# @lc app=leetcode id=3544 lang=python3
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
from typing import List
import sys
sys.setrecursionlimit(10**5 + 10)

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        INF = 10**18
        dp = [[[-INF] * k for _ in range(2)] for _ in range(n)]
        
        def compute(u: int, p: int) -> None:
            for v in adj[u]:
                if v != p:
                    compute(v, u)
            for p_in in range(2):
                for s_in in range(k):
                    max_val = -INF
                    for flip in range(2):
                        if flip == 1 and s_in != 0:
                            continue
                        parity_u = (p_in + flip) % 2
                        contrib_u = nums[u] if parity_u == 0 else -nums[u]
                        p_child = parity_u
                        if flip == 1:
                            s_child = 0 if k <= 1 else 1
                        else:
                            if s_in == 0:
                                s_child = 0
                            else:
                                s_child = 0 if s_in + 1 >= k else s_in + 1
                        children_sum = 0
                        for v in adj[u]:
                            if v != p:
                                children_sum += dp[v][p_child][s_child]
                        total = contrib_u + children_sum
                        max_val = max(max_val, total)
                    dp[u][p_in][s_in] = max_val
        
        compute(0, -1)
        return dp[0][0][0]
# @lc code=end