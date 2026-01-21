#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
from collections import deque

class Solution:
    def maxLen(self, n: int, edges: list[list[int]], label: str) -> int:
        if n == 0:
            return 0
        
        adj = [[] for _ in range(n)]
        adj_by_char = [[[] for _ in range(26)] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            adj_by_char[u][ord(label[v]) - 97].append(v)
            adj_by_char[v][ord(label[u]) - 97].append(u)
            
        # visited[u][v] stores sets of masks for a palindromic path between u and v
        visited = [[set() for _ in range(n)] for _ in range(n)]
        states = [[] for _ in range(n + 1)]
        
        max_len = 1
        
        # Base Case: Length 1
        for i in range(n):
            mask = 1 << i
            states[1].append((mask, i, i))
            visited[i][i].add(mask)
            
        # Base Case: Length 2
        for u, v in edges:
            if label[u] == label[v]:
                mask = (1 << u) | (1 << v)
                if mask not in visited[u][v]:
                    states[2].append((mask, u, v))
                    visited[u][v].add(mask)
                    visited[v][u].add(mask)
                    max_len = 2
        
        # Expand from length L to L+2
        for L in range(1, n - 1):
            if not states[L]:
                continue
            for mask, u, v in states[L]:
                for x in adj[u]:
                    if not (mask & (1 << x)):
                        char_idx = ord(label[x]) - 97
                        for y in adj_by_char[v][char_idx]:
                            if x != y and not (mask & (1 << y)):
                                new_mask = mask | (1 << x) | (1 << y)
                                if new_mask not in visited[x][y]:
                                    visited[x][y].add(new_mask)
                                    visited[y][x].add(new_mask)
                                    states[L + 2].append((new_mask, x, y))
                                    if L + 2 > max_len:
                                        max_len = L + 2
                                        
        return max_len
# @lc code=end