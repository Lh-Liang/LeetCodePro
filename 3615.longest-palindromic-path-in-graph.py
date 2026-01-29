#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
from typing import List
from collections import deque

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        if n == 0: return 0
        
        # Precompute adjacency masks for each node
        adj = [0] * n
        for u, v in edges:
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)
            
        # Group nodes by their labels for fast lookup
        label_masks = [0] * 26
        for i, char in enumerate(label):
            label_masks[ord(char) - ord('a')] |= (1 << i)
            
        queue = deque()
        visited = set()
        max_len = 1
        
        # Base cases: Length 1 (all nodes)
        for i in range(n):
            state = (i, i, 1 << i)
            queue.append(state)
            visited.add(state)
            
        # Base cases: Length 2 (all matching edges)
        for u, v in edges:
            if label[u] == label[v]:
                # Store endpoints in sorted order to reduce state space
                s, e = (u, v) if u < v else (v, u)
                state = (s, e, (1 << u) | (1 << v))
                if state not in visited:
                    queue.append(state)
                    visited.add(state)
                    max_len = 2
                    
        while queue:
            u, v, mask = queue.popleft()
            # Current length is the number of set bits in mask
            curr_len = bin(mask).count('1')
            if curr_len > max_len: 
                max_len = curr_len
            
            # Try to expand the palindrome by adding a matching character to both ends
            for char_idx in range(26):
                char_mask = label_masks[char_idx]
                # Potential neighbors of u and v with the same character
                targets_u = adj[u] & char_mask & ~mask
                if not targets_u: continue
                targets_v = adj[v] & char_mask & ~mask
                if not targets_v: continue
                
                # Extract individual nodes from the target masks
                nodes_u = [i for i in range(n) if (targets_u >> i) & 1]
                nodes_v = [i for i in range(n) if (targets_v >> i) & 1]
                
                for nu in nodes_u:
                    for nv in nodes_v:
                        # Path must use unique nodes
                        if nu != nv:
                            new_u, new_v = (nu, nv) if nu < nv else (nv, nu)
                            new_mask = mask | (1 << nu) | (1 << nv)
                            new_state = (new_u, new_v, new_mask)
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append(new_state)
                                    
        return max_len
# @lc code=end