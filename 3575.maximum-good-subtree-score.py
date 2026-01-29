#
# @lc app=leetcode id=3575 lang=python3
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
import sys

# Increase recursion depth for potential line-graph trees
sys.setrecursionlimit(2000)

class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[par[i]].append(i)
            
        # Precompute digit masks for each node value
        node_masks = []
        for v in vals:
            m = 0
            s = str(v)
            possible = True
            for char in s:
                digit = ord(char) - ord('0')
                if (m >> digit) & 1:
                    possible = False
                    break
                m |= (1 << digit)
            node_masks.append(m if possible else -1)
            
        # Standard DSU on Trees (Sack) preparation
        sz = [1] * n
        heavy = [-1] * n
        tin = [0] * n
        tout = [0] * n
        node_at_tin = [0] * n
        timer = 0
        
        def dfs_sz(u):
            nonlocal timer
            tin[u] = timer
            node_at_tin[timer] = u
            timer += 1
            max_c_sz = -1
            for v in adj[u]:
                dfs_sz(v)
                sz[u] += sz[v]
                if sz[v] > max_c_sz:
                    max_c_sz = sz[v]
                    heavy[u] = v
            tout[u] = timer - 1

        dfs_sz(0)
        
        # Global DP table: dp[mask] = max score for a good subset with digits 'mask'
        dp = [-1] * 1024
        dp[0] = 0
        max_scores = [0] * n
        
        def add_node(u):
            m_i = node_masks[u]
            if m_i == -1:
                return
            v_i = vals[u]
            # Standard 0/1 knapsack bitmask update
            for m in range(1023, -1, -1):
                if dp[m] != -1 and not (m & m_i):
                    nm = m | m_i
                    if dp[m] + v_i > dp[nm]:
                        dp[nm] = dp[m] + v_i
        
        def dfs_sack(u, keep):
            # 1. Process light children and clear their DP state
            for v in adj[u]:
                if v != heavy[u]:
                    dfs_sack(v, False)
            
            # 2. Process heavy child and keep its DP state
            if heavy[u] != -1:
                dfs_sack(heavy[u], True)
            
            # 3. Add nodes from light subtrees and the current node u
            for v in adj[u]:
                if v != heavy[u]:
                    for t in range(tin[v], tout[v] + 1):
                        add_node(node_at_tin[t])
            add_node(u)
            
            # 4. Record max score for subtree rooted at u
            max_scores[u] = max(dp)
            
            # 5. If not the heavy child of its parent, clear the state
            if not keep:
                for i in range(1024):
                    dp[i] = -1
                dp[0] = 0

        dfs_sack(0, True)
        
        MOD = 10**9 + 7
        return sum(max_scores) % MOD
# @lc code=end