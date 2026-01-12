#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
import sys

# Increase recursion depth for deep trees up to 10^5 nodes
sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        if n == 0:
            return []
            
        # Step 1: Build the original tree adjacency list
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        # Step 2: Find new parents based on closest ancestor with same character
        new_parent = list(parent)
        last_seen = [-1] * 26
        
        def find_new_parents(u):
            char_idx = ord(s[u]) - 97  # ord('a') is 97
            
            # Save the current closest ancestor with this character
            old_val = last_seen[char_idx]
            
            # If an ancestor with the same character exists, it becomes the new parent
            if old_val != -1:
                new_parent[u] = old_val
            
            # Update state for children: this node is now the closest ancestor for its character
            last_seen[char_idx] = u
            for v in adj[u]:
                find_new_parents(v)
            
            # Backtrack: restore state for other branches of the DFS
            last_seen[char_idx] = old_val
            
        find_new_parents(0)
        
        # Step 3: Build the final tree adjacency list using updated parents
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        # Step 4: Calculate subtree sizes in the modified tree
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