#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
from typing import List
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def get_color_counts(edges, num_nodes):
            if num_nodes == 0:
                return [], [0, 0]
            adj = [[] for _ in range(num_nodes)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            
            colors = [-1] * num_nodes
            counts = [0, 0]
            
            # Iterative BFS to avoid recursion depth issues
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
        
        colors1, counts1 = get_color_counts(edges1, n)
        _, counts2 = get_color_counts(edges2, m)
        
        # For any node i in Tree 1, we can connect it to a node in Tree 2
        # such that we reach the maximum number of nodes in Tree 2 at an even distance.
        # The distance from i to k in Tree 2 is 1 + dist(bridge_node_in_Tree2, k).
        # We want 1 + dist to be even, so dist must be odd.
        # The max nodes at an odd distance from any node in Tree 2 is max(counts2[0], counts2[1]).
        max_tree2_contribution = max(counts2)
        
        ans = [0] * n
        for i in range(n):
            ans[i] = counts1[colors1[i]] + max_tree2_contribution
            
        return ans
# @lc code=end