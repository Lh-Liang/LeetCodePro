#
# @lc app=leetcode id=3515 lang=python3
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        class FenwickTree:
            def __init__(self, size: int):
                self.size = size
                self.tree = [0] * (size + 2)

            def update(self, index: int, delta: int) -> None:
                while index <= self.size:
                    self.tree[index] += delta
                    index += index & -index

            def query(self, index: int) -> int:
                res = 0
                while index > 0:
                    res += self.tree[index]
                    index -= index & -index
                return res

        import sys
        sys.setrecursionlimit(100010)

        adj = [[] for _ in range(n + 1)]
        weights = {}
        for u, v, w in edges:
            adj[u].append(v)
            adj[v].append(u)
            key = tuple(sorted((u, v)))
            weights[key] = w

        parent = [-1] * (n + 1)
        intime = [0] * (n + 1)
        outtime = [0] * (n + 1)
        timer = [1]

        def dfs(node: int, par: int) -> None:
            parent[node] = par
            intime[node] = timer[0]
            timer[0] += 1
            for nei in adj[node]:
                if nei != par:
                    dfs(nei, node)
            outtime[node] = timer[0]
            timer[0] += 1

        dfs(1, -1)

        ft = FenwickTree(timer[0])

        for node in range(2, n + 1):
            par = parent[node]
            key = tuple(sorted((par, node)))
            w = weights[key]
            ft.update(intime[node], w)
            ft.update(outtime[node], -w)

        ans = []
        for q in queries:
            if q[0] == 1:
                u, v, wnew = q[1], q[2], q[3]
                if parent[v] == u:
                    child = v
                    par_node = u
                else:
                    child = u
                    par_node = v
                key = tuple(sorted((par_node, child)))
                oldw = weights[key]
                delta = wnew - oldw
                weights[key] = wnew
                ft.update(intime[child], delta)
                ft.update(outtime[child], -delta)
            else:
                x = q[1]
                ans.append(ft.query(intime[x]))
        return ans

# @lc code=end