#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dfs(u, parent):
            gains = []
            base_sum = 0
            
            for v, w in graph[u]:
                if v == parent:
                    continue
                val0, val1 = dfs(v, u)
                base_sum += val0
                gain = w + val1 - val0
                gains.append(gain)
            
            gains.sort(reverse=True)
            
            # dp[u][0]: can use at most k edges
            dp0 = base_sum
            for i in range(min(k, len(gains))):
                if gains[i] > 0:
                    dp0 += gains[i]
            
            # dp[u][1]: can use at most k-1 edges
            dp1 = base_sum
            for i in range(min(k-1, len(gains))):
                if gains[i] > 0:
                    dp1 += gains[i]
            
            return dp0, dp1
        
        return dfs(0, -1)[0]
# @lc code=end