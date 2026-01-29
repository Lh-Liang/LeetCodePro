#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
from typing import List

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
        
        # 1. Sort children to ensure they are visited in increasing order
        for i in range(n):
            adj[i].sort()
            
        start_idx = [0] * n
        end_idx = [0] * n
        order = []
        
        # 2. Iterative post-order DFS to build the global string and record node ranges
        # stack stores (node, visited_children_flag)
        stack = [(0, False)]
        timer = 0
        while stack:
            u, visited = stack.pop()
            if not visited:
                # Pre-order: mark the start of this node's contribution in 'order'
                start_idx[u] = timer
                stack.append((u, True))
                # Push children in reverse order so they are processed in increasing order
                for v in reversed(adj[u]):
                    stack.append((v, False))
            else:
                # Post-order: append character and mark the end index
                order.append(s[u])
                end_idx[u] = timer
                timer += 1
        
        # The global string formed by the DFS process
        S = "".join(order)
        
        # 3. Manacher's Algorithm to find all palindromic substrings in O(n)
        # T = # s[0] # s[1] # ... # s[n-1] #
        T = '#' + '#'.join(S) + '#'
        m = len(T)
        P = [0] * m
        center = right = 0
        for i in range(m):
            if i < right:
                P[i] = min(right - i, P[2 * center - i])
            
            while i - P[i] - 1 >= 0 and i + P[i] + 1 < m and T[i - P[i] - 1] == T[i + P[i] + 1]:
                P[i] += 1
            
            if i + P[i] > right:
                center, right = i, i + P[i]
        
        # 4. Check each node's range against the precomputed Manacher radii
        ans = [False] * n
        for i in range(n):
            L, R = start_idx[i], end_idx[i]
            # The substring in S is S[L:R+1]. 
            # In T, the center of S[L:R+1] is at index (L + R + 1).
            # The length of the substring is (R - L + 1).
            m_center = L + R + 1
            m_length = R - L + 1
            if P[m_center] >= m_length:
                ans[i] = True
        
        return ans
# @lc code=end