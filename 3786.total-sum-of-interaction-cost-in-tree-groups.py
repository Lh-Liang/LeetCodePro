#
# @lc app=leetcode id=3786 lang=python3
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

import sys
sys.setrecursionlimit(100010)

from typing import List

# @lc code=start
class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total = [0] * 21
        for i in range(n):
            total[group[i]] += 1
        ans = [0]
        def dfs(node: int, par: int) -> List[int]:
            counts = [0] * 21
            counts[group[node]] += 1
            for nei in adj[node]:
                if nei != par:
                    child_cnt = dfs(nei, node)
                    for g in range(1, 21):
                        a = child_cnt[g]
                        b = total[g] - a
                        ans[0] += a * b
                    for g in range(1, 21):
                        counts[g] += child_cnt[g]
            return counts
        dfs(0, -1)
        return ans[0]
        
# @lc code=end
