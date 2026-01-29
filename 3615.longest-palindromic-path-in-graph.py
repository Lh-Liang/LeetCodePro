#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
from collections import deque

class Solution:
    def maxLen(self, n: int, edges: list[list[int]], label: str) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # State: (mask, u, v) where u <= v
        # mask: bitmask of nodes in the path
        # u, v: endpoints of the palindromic path
        visited = set()
        queue = deque()
        max_len = 1
        
        # Base Case: Length 1
        for i in range(n):
            mask = 1 << i
            state = (mask, i, i)
            visited.add(state)
            queue.append((1, mask, i, i))
            
        # Base Case: Length 2
        for u in range(n):
            for v in adj[u]:
                if u < v and label[u] == label[v]:
                    mask = (1 << u) | (1 << v)
                    state = (mask, u, v)
                    if state not in visited:
                        visited.add(state)
                        queue.append((2, mask, u, v))
                        max_len = max(max_len, 2)
        
        while queue:
            curr_len, mask, u, v = queue.popleft()
            max_len = max(max_len, curr_len)
            
            # Try to expand the palindrome from both ends
            for nu in adj[u]:
                if not (mask & (1 << nu)):
                    for nv in adj[v]:
                        # nu must not be in mask, nv must not be in mask
                        # and nu must not be nv
                        if not (mask & (1 << nv)) and nu != nv:
                            if label[nu] == label[nv]:
                                new_mask = mask | (1 << nu) | (1 << nv)
                                next_u, next_v = (nu, nv) if nu < nv else (nv, nu)
                                new_state = (new_mask, next_u, next_v)
                                
                                if new_state not in visited:
                                    visited.add(new_state)
                                    queue.append((curr_len + 2, new_mask, next_u, next_v))
                                    
        return max_len
# @lc code=end