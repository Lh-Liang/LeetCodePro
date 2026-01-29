#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
import sys

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        # Increase recursion depth for deep trees
        sys.setrecursionlimit(max(200000, n + 1000))
        
        # Build original adjacency list
        original_adj = [[] for _ in range(n)]
        for i in range(1, n):
            original_adj[parent[i]].append(i)
            
        new_parents = [-1] * n
        # last_seen maps character -> stack of ancestor nodes
        last_seen = {chr(ord('a') + i): [] for i in range(26)}
        
        def find_new_parents(u):
            char = s[u]
            if last_seen[char]:
                new_parents[u] = last_seen[char][-1]
            else:
                new_parents[u] = parent[u]
                
            last_seen[char].append(u)
            for v in original_adj[u]:
                find_new_parents(v)
            last_seen[char].pop()
            
        find_new_parents(0)
        
        # Build new adjacency list based on updated parents
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parents[i]].append(i)
            
        subtree_sizes = [0] * n
        
        def calculate_sizes(u):
            size = 1
            for v in new_adj[u]:
                size += calculate_sizes(v)
            subtree_sizes[u] = size
            return size
            
        calculate_sizes(0)
        return subtree_sizes
# @lc code=end