#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#

from typing import List

# @lc code=start
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        currencies = set([initialCurrency])
        for pairs in [pairs1, pairs2]:
            for p in pairs:
                currencies.add(p[0])
                currencies.add(p[1])
        clist = list(currencies)
        C = len(clist)
        idx = {c: i for i, c in enumerate(clist)}
        
        def build_graph(pairs: List[List[str]], rates: List[float]) -> List[List[float]]:
            dist = [[0.0] * C for _ in range(C)]
            for i in range(C):
                dist[i][i] = 1.0
            for k in range(len(pairs)):
                a, b = pairs[k]
                r = rates[k]
                i_ = idx[a]
                j_ = idx[b]
                dist[i_][j_] = max(dist[i_][j_], r)
                dist[j_][i_] = max(dist[j_][i_], 1.0 / r)
            return dist
        
        def floyd_warshall(dist: List[List[float]]) -> List[List[float]]:
            n = len(dist)
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        cand = dist[i][k] * dist[k][j]
                        if cand > dist[i][j]:
                            dist[i][j] = cand
            return dist
        
        m1 = build_graph(pairs1, rates1)
        m1 = floyd_warshall(m1)
        m2 = build_graph(pairs2, rates2)
        m2 = floyd_warshall(m2)
        
        s = idx[initialCurrency]
        max_amt = 1.0
        for x in range(C):
            total = m1[s][x] * m2[x][s]
            if total > max_amt:
                max_amt = total
        return max_amt
# @lc code=end
