#
# @lc app=leetcode id=3387 lang=python3
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        currencies = set([initialCurrency])
        for pairs in (pairs1, pairs2):
            for pair in pairs:
                currencies.add(pair[0])
                currencies.add(pair[1])
        curr_list = sorted(currencies)
        K = len(curr_list)
        idx = {curr: i for i, curr in enumerate(curr_list)}
        s = idx[initialCurrency]

        def fw(adj):
            dist = [row[:] for row in adj]
            for k in range(K):
                for i in range(K):
                    for j in range(K):
                        if dist[i][k] > 0.0 and dist[k][j] > 0.0:
                            dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])
            return dist

        adj1 = [[0.0] * K for _ in range(K)]
        for i in range(len(pairs1)):
            a, b = pairs1[i]
            ia, ib = idx[a], idx[b]
            r = rates1[i]
            adj1[ia][ib] = max(adj1[ia][ib], r)
            adj1[ib][ia] = max(adj1[ib][ia], 1 / r)
        for i in range(K):
            adj1[i][i] = 1.0
        dist1 = fw(adj1)

        adj2 = [[0.0] * K for _ in range(K)]
        for i in range(len(pairs2)):
            a, b = pairs2[i]
            ia, ib = idx[a], idx[b]
            r = rates2[i]
            adj2[ia][ib] = max(adj2[ia][ib], r)
            adj2[ib][ia] = max(adj2[ib][ia], 1 / r)
        for i in range(K):
            adj2[i][i] = 1.0
        dist2 = fw(adj2)

        ans = 1.0
        for c in range(K):
            ans = max(ans, dist1[s][c] * dist2[c][s])
        return ans
# @lc code=end