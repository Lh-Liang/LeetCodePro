#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
        
        for i in range(n):
            adj[i].sort()
            
        dfs_order_chars = []
        intervals = [None] * n
        
        def build_dfs_string(u):
            start = len(dfs_order_chars)
            for v in adj[u]:
                build_dfs_string(v)
            dfs_order_chars.append(s[u])
            end = len(dfs_order_chars) - 1
            intervals[u] = (start, end)
            
        build_dfs_string(0)
        
        t = "".join(dfs_order_chars)
        rev_t = t[::-1]
        
        # Rolling Hash Parameters
        P = 31
        MOD = 10**9 + 7
        
        pow_p = [1] * (n + 1)
        h_fwd = [0] * (n + 1)
        h_bwd = [0] * (n + 1)
        
        for i in range(n):
            pow_p[i+1] = (pow_p[i] * P) % MOD
            h_fwd[i+1] = (h_fwd[i] * P + (ord(t[i]) - ord('a') + 1)) % MOD
            h_bwd[i+1] = (h_bwd[i] * P + (ord(rev_t[i]) - ord('a') + 1)) % MOD
            
        def get_hash(h, l, r):
            # Hash of substring t[l:r+1]
            res = (h[r+1] - h[l] * pow_p[r - l + 1]) % MOD
            return res

        ans = [False] * n
        for i in range(n):
            l, r = intervals[i]
            # The reverse of t[l:r+1] is rev_t[(n-1-r):(n-1-l)+1]
            l_rev, r_rev = n - 1 - r, n - 1 - l
            if get_hash(h_fwd, l, r) == get_hash(h_bwd, l_rev, r_rev):
                ans[i] = True
                
        return ans
# @lc code=end