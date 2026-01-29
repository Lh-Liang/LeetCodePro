#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def get_partition_sizes(edges, num_nodes):
            adj = [[] for _ in range(num_nodes)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            
            colors = [-1] * num_nodes
            colors[0] = 0
            queue = deque([0])
            count0 = 0
            while queue:
                u = queue.popleft()
                if colors[u] == 0:
                    count0 += 1
                for v in adj[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
            
            count1 = num_nodes - count0
            return colors, count0, count1

        n = len(edges1) + 1
        m = len(edges2) + 1
        
        colors1, c1_0, c1_1 = get_partition_sizes(edges1, n)
        _, c2_0, c2_1 = get_partition_sizes(edges2, m)
        
        max_tree2_contribution = max(c2_0, c2_1)
        
        results = [0] * n
        for i in range(n):
            if colors1[i] == 0:
                results[i] = c1_0 + max_tree2_contribution
            else:
                results[i] = c1_1 + max_tree2_contribution
        
        return results
# @lc code=end