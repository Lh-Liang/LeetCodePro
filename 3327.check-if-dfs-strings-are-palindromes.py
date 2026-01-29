#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
import random
from typing import List

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
        
        # Ensure children are visited in increasing order
        for i in range(n):
            if len(adj[i]) > 1:
                adj[i].sort()
        
        start_idx = [0] * n
        end_idx = [0] * n
        dfs_sequence = []
        
        # Iterative post-order DFS to build the global string and track subtree ranges
        # state 0: pre-order (record start), state 1: post-order (append char and record end)
        stack = [(0, 0)]
        while stack:
            u, state = stack.pop()
            if state == 0:
                start_idx[u] = len(dfs_sequence)
                stack.append((u, 1))
                # Push children in reverse for LIFO to process in increasing order
                curr_children = adj[u]
                for i in range(len(curr_children) - 1, -1, -1):
                    stack.append((curr_children[i], 0))
            else:
                dfs_sequence.append(s[u])
                end_idx[u] = len(dfs_sequence) - 1
        
        m = len(dfs_sequence)
        MOD = (1 << 61) - 1
        BASE = random.randint(31, 1000)
        
        # Precompute powers and forward/backward rolling hashes
        pows = [1] * (m + 1)
        fwd_hashes = [0] * (m + 1)
        rev_hashes = [0] * (m + 1)
        
        # Forward hash construction
        for i in range(m):
            val = ord(dfs_sequence[i]) - 96
            fwd_hashes[i+1] = (fwd_hashes[i] * BASE + val) % MOD
            pows[i+1] = (pows[i] * BASE) % MOD
            
        # Backward hash construction (using reversed sequence)
        rev_sequence = dfs_sequence[::-1]
        for i in range(m):
            val = ord(rev_sequence[i]) - 96
            rev_hashes[i+1] = (rev_hashes[i] * BASE + val) % MOD
            
        ans = [False] * n
        for i in range(n):
            L, R = start_idx[i], end_idx[i]
            length = R - L + 1
            
            # Extract forward hash for range [L, R]
            h_fwd = (fwd_hashes[R+1] - fwd_hashes[L] * pows[length]) % MOD
            
            # Map range [L, R] to the reversed string's indices
            # S[L...R] reversed is S_rev[m-1-R ... m-1-L]
            L_rev, R_rev = m - 1 - R, m - 1 - L
            h_rev = (rev_hashes[R_rev+1] - rev_hashes[L_rev] * pows[length]) % MOD
            
            if h_fwd == h_rev:
                ans[i] = True
                
        return ans
# @lc code=end