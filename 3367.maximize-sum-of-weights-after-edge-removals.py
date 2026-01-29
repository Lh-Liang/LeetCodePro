#
# @lc app=leetcode id=3367 lang=python3
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
import sys
import collections
from typing import List

class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Increase recursion depth for deep trees (n up to 10^5)
        sys.setrecursionlimit(200000)
        
        def dfs(u, p):
            base_sum = 0
            gains = []
            
            for v, w in adj[u]:
                if v == p:
                    continue
                
                # d0: child v can use up to k edges (edge u-v is NOT kept)
                # d1: child v can use up to k-1 edges (edge u-v IS kept)
                d0, d1 = dfs(v, u)
                
                # Start by assuming we don't keep the edge to the child
                base_sum += d0
                
                # Calculate the potential gain if we decide to keep edge (u, v)
                # Gain = (Weight + Max sum of child with k-1 edges) - (Max sum of child with k edges)
                gain = w + d1 - d0
                if gain > 0:
                    gains.append(gain)
            
            # Sort gains descending to pick the most valuable edges to keep
            gains.sort(reverse=True)
            
            # dp[u][0]: Max sum if u can use at most k edges
            res0 = base_sum + sum(gains[:k])
            
            # dp[u][1]: Max sum if u can use at most k-1 edges (to allow parent edge)
            res1 = base_sum + sum(gains[:k-1])
            
            return res0, res1
            
        ans0, _ = dfs(0, -1)
        return ans0
# @lc code=end