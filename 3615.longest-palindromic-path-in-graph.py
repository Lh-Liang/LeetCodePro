#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
from collections import deque

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Use set to track visited states
        # dp stores (mask, i, j) where there's a palindrome path using nodes in mask
        # starting at node i and ending at node j
        dp = set()
        queue = deque()
        
        # Base case 1: single node (odd-length palindrome center)
        for i in range(n):
            mask = 1 << i
            dp.add((mask, i, i))
            queue.append((mask, i, i))
        
        # Base case 2: two adjacent nodes with same label (even-length palindrome center)
        for u, v in edges:
            if label[u] == label[v]:
                mask = (1 << u) | (1 << v)
                if (mask, u, v) not in dp:
                    dp.add((mask, u, v))
                    queue.append((mask, u, v))
                if (mask, v, u) not in dp:
                    dp.add((mask, v, u))
                    queue.append((mask, v, u))
        
        ans = 1  # At least single node is a palindrome
        
        # BFS to expand palindromes from center outward
        while queue:
            mask, i, j = queue.popleft()
            ans = max(ans, bin(mask).count('1'))
            
            # Try to extend by adding matching characters at both ends
            for i_prime in adj[i]:
                if mask & (1 << i_prime):
                    continue  # i_prime already used
                for j_prime in adj[j]:
                    if mask & (1 << j_prime):
                        continue  # j_prime already used
                    if i_prime == j_prime:
                        continue  # Can't use same node twice
                    if label[i_prime] == label[j_prime]:
                        new_mask = mask | (1 << i_prime) | (1 << j_prime)
                        if (new_mask, i_prime, j_prime) not in dp:
                            dp.add((new_mask, i_prime, j_prime))
                            queue.append((new_mask, i_prime, j_prime))
        
        return ans
# @lc code=end