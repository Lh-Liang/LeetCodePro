#
# @lc app=leetcode id=3786 lang=python3
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

from typing import List
from array import array

# @lc code=start
class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        if n <= 1:
            return 0

        K = 20  # group labels are 1..20

        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Total counts per group
        total = [0] * K

        # Flattened subtree counts: counts[node*K + k]
        counts = array('I', [0]) * (n * K)
        for i, g in enumerate(group):
            idx = g - 1
            total[idx] += 1
            counts[i * K + idx] = 1

        # Iterative DFS to get parent and traversal order
        parent = [-1] * n
        order = []
        stack = [0]
        parent[0] = 0
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                stack.append(v)

        # Postorder accumulate counts and compute answer
        ans = 0
        for i in range(n - 1, 0, -1):  # skip root at index 0
            u = order[i]
            p = parent[u]
            bu = u * K
            bp = p * K
            for k in range(K):
                x = counts[bu + k]
                if x:
                    ans += x * (total[k] - x)
                    counts[bp + k] += x

        return ans
# @lc code=end
