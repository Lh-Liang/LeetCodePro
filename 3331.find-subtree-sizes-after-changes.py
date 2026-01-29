#
# @lc app=leetcode id=3331 lang=python3
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
        
        # Step 1: Determine new parents based on original tree structure
        new_parent = [-1] * n
        last_seen = [[] for _ in range(26)]
        
        # Iterative DFS to find the closest same-character ancestor
        # Stack stores (node, is_processed)
        stack = [(0, False)]
        while stack:
            u, processed = stack.pop()
            char_idx = ord(s[u]) - ord('a')
            
            if not processed:
                # Pre-order: determine new parent
                if last_seen[char_idx]:
                    new_parent[u] = last_seen[char_idx][-1]
                else:
                    new_parent[u] = parent[u]
                
                # Push back to handle post-order cleanup and push children
                last_seen[char_idx].append(u)
                stack.append((u, True))
                for v in adj[u]:
                    stack.append((v, False))
            else:
                # Post-order: cleanup last_seen for this character
                last_seen[char_idx].pop()
        
        # Step 2: Build the adjacency list for the modified tree
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        # Step 3: Calculate subtree sizes in the new tree using post-order traversal
        subtree_size = [1] * n
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in new_adj[u]:
                stack.append(v)
        
        # Process nodes in reverse topological order (leaves to root)
        for u in reversed(order):
            p = new_parent[u]
            if p != -1:
                subtree_size[p] += subtree_size[u]
                
        return subtree_size
# @lc code=end