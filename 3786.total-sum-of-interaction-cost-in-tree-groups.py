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

        group2nodes = defaultdict(list)
        for i, g in enumerate(group):
            group2nodes[g].append(i)

        res = 0
        visited_global = [False] * n
        for g, nodes in group2nodes.items():
            in_group = [False] * n
            for u in nodes:
                in_group[u] = True
            visited = [False] * n
            def dfs(u):
                visited[u] = True
                cnt = 1 if in_group[u] else 0
                for v in adj[u]:
                    if not visited[v]:
                        c = dfs(v)
                        # Each edge (u-v) contributes c * (total_in_group - c) for this group
                        edge_contrib = c * (total_in_group - c)
                        nonlocal res
                        res += edge_contrib
                        cnt += c
                return cnt
            total_in_group = len(nodes)
            for u in nodes:
                if not visited[u]:
                    dfs(u)
        return res
# @lc code=end