#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = defaultdict(list)
        
        # Step 1: Build initial adjacency list representation of tree
        for i in range(1, n):
            adj[parent[i]].append(i)
        
        # Step 2: Update parents based on character matching rule
        new_parent = parent[:]
        for x in range(1, n):
            current = x
            while current != -1:
                if current != x and s[current] == s[x]:
                    new_parent[x] = current
                    break
                current = parent[current]
            else:
                new_parent[x] = parent[x]
        
        # Step 3: Build new adjacency list with updated parents
        new_adj = defaultdict(list)
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
        
        # Step 4 & 5: Calculate subtree sizes using DFS on modified tree structure once from root node (0)
        def dfs(node):
            size = 1 # Count itself initially
            for neighbor in new_adj[node]:
                size += dfs(neighbor) # Recursively add children sizes
            result[node] = size # Record size of the subtree rooted at this node
            return size
        
        result = [0] * n
        dfs(0) # Calculate from root (node 0)
        return result # Return final subtree sizes after modifications are applied
# @lc code=end