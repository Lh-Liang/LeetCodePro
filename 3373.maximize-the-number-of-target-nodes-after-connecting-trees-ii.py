#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
import collections
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def get_tree_stats(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            
            colors = [-1] * n
            counts = [0, 0]
            
            # Standard BFS to 2-color the tree
            queue = collections.deque([0])
            colors[0] = 0
            counts[0] = 1
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        counts[colors[v]] += 1
                        queue.append(v)
            return colors, counts

        n = len(edges1) + 1
        colors1, counts1 = get_tree_stats(edges1)
        
        # For Tree 2, we only care about the size of the larger color partition
        _, counts2 = get_tree_stats(edges2)
        max_tree2_contribution = max(counts2)
        
        # The answer for node i is (nodes in Tree 1 with same color as i) + (max parity set in Tree 2)
        return [counts1[colors1[i]] + max_tree2_contribution for i in range(n)]
# @lc code=end