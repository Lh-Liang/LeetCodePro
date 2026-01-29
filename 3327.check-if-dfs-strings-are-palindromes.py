#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
        
        # Children must be visited in increasing order
        for i in range(n):
            adj[i].sort()

        # Iterative post-order DFS to build post-order string P and track subtree sizes
        P = []
        end_pos = [0] * n
        size = [1] * n
        stack = [(0, 0)]  # (node, state: 0 for pre-order, 1 for post-order)
        
        while stack:
            u, state = stack.pop()
            if state == 0:
                stack.append((u, 1))
                # Push children in reverse to process them in increasing order
                for v in reversed(adj[u]):
                    stack.append((v, 0))
            else:
                P.append(s[u])
                end_pos[u] = len(P) - 1
                p_idx = parent[u]
                if p_idx != -1:
                    size[p_idx] += size[u]
        
        # Manacher's Algorithm to find palindromes in O(n)
        s_P = "".join(P)
        T = "#" + "#".join(s_P) + "#"
        m = len(T)
        d = [0] * m
        l, r = 0, -1
        for i in range(m):
            k = 1 if i > r else min(d[l + r - i], r - i + 1)
            while 0 <= i - k and i + k < m and T[i - k] == T[i + k]:
                k += 1
            d[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1
        
        ans = [False] * n
        for i in range(n):
            sz = size[i]
            # Substring in P is [L, R]
            R = end_pos[i]
            L = R - sz + 1
            # Center in T is L + R + 1
            center_in_T = L + R + 1
            if d[center_in_T] >= sz + 1:
                ans[i] = True
        
        return ans
# @lc code=end