#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start

from collections import deque


class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        chars = set()
        for w in words:
            chars.add(w[0])
            chars.add(w[1])
        char_list = sorted(chars)
        m = len(char_list)
        if m == 0:
            return []
        c2i = {char_list[i]: i for i in range(m)}
        has_edge = [[False] * m for _ in range(m)]
        for w in words:
            u = c2i[w[0]]
            v = c2i[w[1]]
            has_edge[u][v] = True
        min_L = float('inf')
        cand = []
        for mask in range(1 << m):
            num_doubles = bin(mask).count('1')
            L = m + num_doubles
            adj = [[] for _ in range(2 * m)]
            indeg = [0] * (2 * m)
            for i in range(m):
                if mask & (1 << i):
                    s = i
                    e = m + i
                    adj[s].append(e)
                    indeg[e] += 1
            for u in range(m):
                for v in range(m):
                    if has_edge[u][v]:
                        A = u
                        B = m + v if (mask & (1 << v)) else v
                        adj[A].append(B)
                        indeg[B] += 1
            q = deque()
            for node in range(2 * m):
                if indeg[node] == 0 and (node < m or (mask & (1 << (node - m)))):
                    q.append(node)
            visited = 0
            while q:
                node = q.popleft()
                visited += 1
                for nei in adj[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0 and (nei < m or (mask & (1 << (nei - m)))):
                        q.append(nei)
            total_active = m + num_doubles
            if visited == total_active:
                freq = [0] * 26
                for i in range(m):
                    idx = ord(char_list[i]) - ord('a')
                    freq[idx] = 2 if (mask & (1 << i)) else 1
                if L < min_L:
                    min_L = L
                    cand = [freq]
                elif L == min_L:
                    cand.append(freq)
        # Consistency check and deduplication
        if cand:
            expected_sum = min_L
            seen = set()
            res = []
            for f in cand:
                if sum(f) == expected_sum:
                    ft = tuple(f)
                    if ft not in seen:
                        seen.add(ft)
                        res.append(f)
            return res
        return []
# @lc code=end