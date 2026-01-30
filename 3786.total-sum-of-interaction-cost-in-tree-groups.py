#
# @lc app=leetcode id=3786 lang=python3
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(1 << 20)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        res = 0
        group_to_nodes = defaultdict(list)
        for i, g in enumerate(group):
            group_to_nodes[g].append(i)

        for g, nodes in group_to_nodes.items():
            if len(nodes) < 2:
                continue
            in_group = [0] * n
            for u in nodes:
                in_group[u] = 1
            total_count = len(nodes)
            def dfs(u, parent):
                cnt = in_group[u]
                for v in adj[u]:
                    if v == parent: continue
                    sub = dfs(v, u)
                    res_contrib = sub * (total_count - sub)
                    nonlocal res
                    res += res_contrib
                    cnt += sub
                return cnt
            dfs(nodes[0], -1)
        return res
# @lc code=end