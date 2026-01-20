#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
from typing import List

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        N = 1 << n
        NN = n * n
        dp = [False] * (N * NN)

        def get_idx(mask: int, u: int, v: int) -> int:
            return mask * NN + u * n + v

        pop = [0] * N
        for mask in range(N):
            pop[mask] = pop[mask >> 1] + (mask & 1)

        ans = 1
        # Base: single nodes
        for i in range(n):
            mask = 1 << i
            idx = get_idx(mask, i, i)
            dp[idx] = True

        # Base: length 2
        for a in range(n):
            for b in graph[a]:
                if a < b and label[a] == label[b]:
                    mask = (1 << a) | (1 << b)
                    idx_ab = get_idx(mask, a, b)
                    idx_ba = get_idx(mask, b, a)
                    dp[idx_ab] = True
                    dp[idx_ba] = True
                    ans = 2

        # Fill DP
        for mask in range(N):
            for u in range(n):
                if (mask & (1 << u)) == 0:
                    continue
                for v in range(n):
                    if (mask & (1 << v)) == 0:
                        continue
                    idx = get_idx(mask, u, v)
                    if not dp[idx]:
                        continue
                    # Extend
                    for x in graph[u]:
                        if (mask & (1 << x)) != 0:
                            continue
                        lx = label[x]
                        for y in graph[v]:
                            if y == x or (mask & (1 << y)) != 0 or label[y] != lx:
                                continue
                            newmask = mask | (1 << x) | (1 << y)
                            newidx = get_idx(newmask, x, y)
                            if not dp[newidx]:
                                dp[newidx] = True
                                ans = max(ans, pop[newmask])
        return ans
# @lc code=end
