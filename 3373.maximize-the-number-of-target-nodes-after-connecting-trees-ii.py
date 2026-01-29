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
        def get_bipartite_counts(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            
            # colors[i] stores the partition (0 or 1) for node i
            colors = [-1] * n
            counts = [0, 0]
            
            # BFS to color the tree and count nodes in each partition
            # Since it's a tree, it's guaranteed to be bipartite
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

        # Process Tree 1: Get partition assignment for each node and total counts
        colors1, counts1 = get_bipartite_counts(edges1)
        
        # Process Tree 2: Get total partition counts
        _, counts2 = get_bipartite_counts(edges2)
        
        # For any node i in Tree 1, we can connect it to a node j in Tree 2
        # such that we capture all nodes in the larger partition of Tree 2.
        # The distance through the bridge is 1 (odd), so an odd distance in Tree 2
        # results in an even total distance.
        max_from_tree2 = max(counts2)
        n = len(edges1) + 1
        
        # answer[i] = (nodes in i's partition in T1) + (nodes in largest partition in T2)
        return [counts1[colors1[i]] + max_from_tree2 for i in range(n)]
# @lc code=end