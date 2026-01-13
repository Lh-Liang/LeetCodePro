#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

from typing import List
from collections import deque

# @lc code=start
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        allMask = (1 << n) - 1

        # adjacency as bitmask
        adj = [0] * n
        for u, v in edges:
            adj[u] |= 1 << v
            adj[v] |= 1 << u

        # neighbors grouped by character:
        # neighDict[i][c] = bitmask of neighbors of i whose label is c
        neighDict = [dict() for _ in range(n)]
        neighItems = [[] for _ in range(n)]
        for i in range(n):
            d = {}
            m = adj[i]
            while m:
                lsb = m & -m
                j = lsb.bit_length() - 1
                m -= lsb
                c = ord(label[j]) - 97
                d[c] = d.get(c, 0) | lsb
            neighDict[i] = d
            neighItems[i] = list(d.items())  # iterate only existing chars

        # popcount precompute
        pc = [0] * (1 << n)
        for m in range(1, 1 << n):
            pc[m] = pc[m >> 1] + (m & 1)

        # dp[(mask, l)] is a bitset over r (stored in a flattened array)
        dp = [0] * ((1 << n) * n)
        q = deque()

        def add_state(mask: int, l: int, r: int) -> None:
            idx = mask * n + l
            bit = 1 << r
            if dp[idx] & bit:
                return
            dp[idx] |= bit
            q.append((mask, l, r))

        # base: length 1
        for i in range(n):
            add_state(1 << i, i, i)

        # base: length 2 (only one orientation per undirected edge)
        for u, v in edges:
            if label[u] == label[v]:
                l, r = (u, v) if u < v else (v, u)
                add_state((1 << u) | (1 << v), l, r)

        ans = 1
        while q:
            mask, l, r = q.popleft()
            ans = max(ans, pc[mask])

            free = allMask ^ mask

            # try extending by matching characters on both ends
            for c, leftMaskAll in neighItems[l]:
                leftAvail = leftMaskAll & free
                if not leftAvail:
                    continue

                rightMaskAll = neighDict[r].get(c, 0)
                rightAvail = rightMaskAll & free
                if not rightAvail:
                    continue

                aBits = leftAvail
                while aBits:
                    aBit = aBits & -aBits
                    a = aBit.bit_length() - 1
                    aBits -= aBit

                    bBits = rightAvail & ~aBit  # ensure a != b
                    while bBits:
                        bBit = bBits & -bBits
                        b = bBit.bit_length() - 1
                        bBits -= bBit

                        newMask = mask | aBit | bBit
                        add_state(newMask, a, b)

        return ans
# @lc code=end
