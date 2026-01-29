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
        for u in range(n):
            adj[u].sort()
        MOD1 = 1000000007
        MOD2 = 1000000009
        BASE1 = 31
        BASE2 = 37
        len_sub = [0] * n
        hf1 = [0] * n
        hf2 = [0] * n
        hr1 = [0] * n
        hr2 = [0] * n
        import sys
        sys.setrecursionlimit(100010)
        def dfs(u: int) -> None:
            for c in adj[u]:
                dfs(c)
            # compute fwd hash
            h1 = 0
            h2 = 0
            child_len_sum = 0
            for c in adj[u]:
                cl = len_sub[c]
                p1 = pow(BASE1, cl, MOD1)
                h1 = (h1 * p1 + hf1[c]) % MOD1
                p2 = pow(BASE2, cl, MOD2)
                h2 = (h2 * p2 + hf2[c]) % MOD2
                child_len_sum += cl
            ch = ord(s[u]) - ord('a') + 1
            h1 = (h1 * BASE1 + ch) % MOD1
            h2 = (h2 * BASE2 + ch) % MOD2
            len_sub[u] = child_len_sum + 1
            hf1[u] = h1
            hf2[u] = h2
            # compute rev hash
            r1 = ch % MOD1
            r2 = ch % MOD2
            for c in reversed(adj[u]):
                cl = len_sub[c]
                p1 = pow(BASE1, cl, MOD1)
                r1 = (r1 * p1 + hr1[c]) % MOD1
                p2 = pow(BASE2, cl, MOD2)
                r2 = (r2 * p2 + hr2[c]) % MOD2
            hr1[u] = r1
            hr2[u] = r2
        dfs(0)
        answer = [False] * n
        for i in range(n):
            if hf1[i] == hr1[i] and hf2[i] == hr2[i]:
                answer[i] = True
        return answer
# @lc code=end