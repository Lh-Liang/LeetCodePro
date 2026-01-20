#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
from functools import lru_cache
from typing import List

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Precompute neighbors grouped by their character label for faster lookup
        # neighbors[u][char_code] will store a list of neighbors of u that have that label
        neighbors = [[[] for _ in range(26)] for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                char_idx = ord(label[v]) - ord('a')
                neighbors[u][char_idx].append(v)
        
        # DFS with memoization to find the longest extension
        # State: (u, v, mask)
        # u, v: current endpoints of the path (u <= v enforced for uniqueness)
        # mask: bitmask of visited nodes
        @lru_cache(None)
        def dfs(u, v, mask):
            max_extension = 0
            
            # Try to extend from u to nu and v to nv such that label[nu] == label[nv]
            # Iterate through all possible characters 'a'...'z'
            for char_idx in range(26):
                u_candidates = neighbors[u][char_idx]
                if not u_candidates: continue
                
                v_candidates = neighbors[v][char_idx]
                if not v_candidates: continue
                
                for nu in u_candidates:
                    # If nu is already visited, skip
                    if (mask >> nu) & 1:
                        continue
                    
                    for nv in v_candidates:
                        # If nv is already visited, skip
                        if (mask >> nv) & 1:
                            continue
                        
                        # Cannot extend to the same node from both ends (unless it's the center, handled separately)
                        if nu == nv:
                            continue
                            
                        # Determine next state, ensuring first endpoint index < second endpoint index
                        next_u, next_v = (nu, nv) if nu < nv else (nv, nu)
                        new_mask = mask | (1 << nu) | (1 << nv)
                        
                        max_extension = max(max_extension, 2 + dfs(next_u, next_v, new_mask))
            
            return max_extension

        ans = 1
        
        # 1. Try odd-length palindromes centered at each node
        for i in range(n):
            # Path starts at i, length 1. Try to extend.
            ans = max(ans, 1 + dfs(i, i, 1 << i))
            
        # 2. Try even-length palindromes centered at each edge with matching labels
        for u, v in edges:
            if label[u] == label[v]:
                # Path starts at u-v, length 2. Try to extend.
                u_sorted, v_sorted = (u, v) if u < v else (v, u)
                ans = max(ans, 2 + dfs(u_sorted, v_sorted, (1 << u) | (1 << v)))
                
        return ans
# @lc code=end