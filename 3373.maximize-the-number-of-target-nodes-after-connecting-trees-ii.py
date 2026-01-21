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
        def get_colors_and_counts(num_nodes, edges):
            adj = [[] for _ in range(num_nodes)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            
            colors = [-1] * num_nodes
            counts = [0, 0]
            
            # Since it's a tree, it's connected and bipartite.
            # We can start BFS from any node, say node 0.
            queue = deque([0])
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
        m = len(edges2) + 1

        colors1, counts1 = get_colors_and_counts(n, edges1)
        colors2, counts2 = get_colors_and_counts(m, edges2)
        
        # For any node i in Tree 1, we can always connect Tree 1 to Tree 2 
        # such that we pick the color partition in Tree 2 with the maximum number of nodes.
        max_tree2_targets = max(counts2)
        
        ans = []
        for i in range(n):
            # Target nodes in Tree 1 are those with the same parity as node i.
            targets1 = counts1[colors1[i]]
            ans.append(targets1 + max_tree2_targets)
            
        return ans
# @lc code=end