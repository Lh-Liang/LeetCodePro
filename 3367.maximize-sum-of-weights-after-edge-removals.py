#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
import sys
sys.setrecursionlimit(100010)
from typing import List
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))
        def dfs(u, p):
            deltas = []
            sum_a = 0
            for v, w in adj[u]:
                if v == p:
                    continue
                a_v, b_v = dfs(v, u)
                delta = w + b_v - a_v
                deltas.append(delta)
                sum_a += a_v
            deltas.sort(reverse=True)
            m = len(deltas)
            prefix = [0] * (m + 1)
            for i in range(1, m + 1):
                prefix[i] = prefix[i - 1] + deltas[i - 1]
            max_idx_a = min(k, m)
            a_u = sum_a + max(prefix[j] for j in range(max_idx_a + 1))
            max_idx_b = min(k - 1, m)
            b_u = sum_a + max(prefix[j] for j in range(max_idx_b + 1))
            return a_u, b_u
        return dfs(0, -1)[0]

# @lc code=end