#
# @lc app=leetcode id=3786 lang=python3
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        import sys
        sys.setrecursionlimit(10**5 + 10)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        total = [0] * 21
        for i in range(n):
            total[group[i]] += 1
        res = [0]
        def dfs(node, par):
            sub = [0] * 21
            sub[group[node]] = 1
            for nei in adj[node]:
                if nei != par:
                    subnei = dfs(nei, node)
                    for g in range(1, 21):
                        cnt = subnei[g]
                        res[0] += cnt * (total[g] - cnt)
                        sub[g] += cnt
            return sub
        dfs(0, -1)
        return res[0]
# @lc code=end