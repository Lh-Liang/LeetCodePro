#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

from typing import List

# @lc code=start
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        parent = [-1] * n
        order = []
        st = [0]
        parent[0] = -2  # mark root visited

        # Build parent array and traversal order
        while st:
            u = st.pop()
            order.append(u)
            for v, w in adj[u]:
                if v == parent[u]:
                    continue
                if parent[v] != -1:
                    continue
                parent[v] = u
                st.append(v)

        parent[0] = -1

        dp0 = [0] * n  # parent edge not kept
        dp1 = [0] * n  # parent edge kept

        for u in reversed(order):
            base = 0
            gains = []
            for v, w in adj[u]:
                if v == parent[u]:
                    continue
                base += dp0[v]
                gain = dp1[v] + w - dp0[v]
                if gain > 0:
                    gains.append(gain)

            gains.sort(reverse=True)
            m = len(gains)
            pref = [0] * (m + 1)
            for i, g in enumerate(gains, 1):
                pref[i] = pref[i - 1] + g

            take0 = min(k, m)
            dp0[u] = base + pref[take0]

            take1 = min(k - 1, m) if k > 0 else 0
            dp1[u] = base + pref[take1]

        return dp0[0]
# @lc code=end
