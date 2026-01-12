#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
from collections import deque, defaultdict
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def get_parities(edges, n):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            
            parities = [-1] * n
            counts = [0, 0] # counts[0] for parity 0, counts[1] for parity 1
            
            # Since it's a tree, it's connected. One BFS from node 0 suffices.
            queue = deque([(0, 0)])
            parities[0] = 0
            counts[0] = 1
            
            while queue:
                u, p = queue.popleft()
                next_p = 1 - p
                for v in adj[u]:
                    if parities[v] == -1:
                        parities[v] = next_p
                        counts[next_p] += 1
                        queue.append((v, next_p))
            return parities, counts

        n = len(edges1) + 1
        m = len(edges2) + 1
        
        parities1, counts1 = get_parities(edges1, n)
        _, counts2 = get_parities(edges2, m)
        
        # Max target nodes from Tree 2 is max(nodes with dist odd from some j)
        # If we pick j such that its color is 0, nodes at odd distance are those with color 1 (count2[1]).
        # If we pick j such that its color is 1, nodes at odd distance are those with color 0 (count2[0]).
        max_from_tree2 = max(counts2[0], counts2[1])
        
        ans = []
        for i in range(n):
            # Target nodes in Tree 1 are those with same parity as node i
            p = parities1[i]
            ans.append(counts1[p] + max_from_tree2)
            
        return ans
# @lc code=end