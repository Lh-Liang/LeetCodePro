#
# @lc app=leetcode id=3515 lang=python3
#
# [3515] Shortest Path in a Weighted Tree
#

from typing import List

# @lc code=start
class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        # i is 1-indexed
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:
        # prefix sum up to i (1-indexed)
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        parent = [0] * (n + 1)
        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        dist0 = [0] * (n + 1)
        wToPar = [0] * (n + 1)  # weight of edge (parent[node], node)

        # Iterative DFS to compute parent, tin/tout, dist0
        time = 0
        stack = [(1, 0, 0, 0)]  # (node, par, w_par, state) state 0=enter,1=exit
        parent[1] = 0
        dist0[1] = 0
        wToPar[1] = 0

        while stack:
            u, p, wp, state = stack.pop()
            if state == 0:
                parent[u] = p
                wToPar[u] = wp
                tin[u] = time
                time += 1
                stack.append((u, p, wp, 1))
                # push children
                for v, w in adj[u][::-1]:
                    if v == p:
                        continue
                    dist0[v] = dist0[u] + w
                    stack.append((v, u, w, 0))
            else:
                tout[u] = time - 1

        # BIT over Euler indices [0..n-1] using range-add / point-query
        bit = Fenwick(n + 2)

        def range_add(l0: int, r0: int, delta: int) -> None:
            # l0,r0 are 0-indexed inclusive
            l = l0 + 1
            r_plus_1 = r0 + 2
            bit.add(l, delta)
            bit.add(r_plus_1, -delta)

        def point(pos0: int) -> int:
            return bit.sum(pos0 + 1)

        ans = []
        for q in queries:
            if q[0] == 1:
                _, u, v, wnew = q
                # determine child endpoint in rooted tree
                if parent[u] == v:
                    child = u
                else:
                    child = v
                delta = wnew - wToPar[child]
                if delta != 0:
                    wToPar[child] = wnew
                    range_add(tin[child], tout[child], delta)
            else:
                _, x = q
                ans.append(dist0[x] + point(tin[x]))

        return ans
# @lc code=end
