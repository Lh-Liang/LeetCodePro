#
# @lc app=leetcode id=3534 lang=python3
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
from typing import List
import bisect

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        nodes = sorted(range(n), key=lambda x: nums[x])
        rank = [0] * n
        for r, node in enumerate(nodes):
            rank[node] = r
        val = [nums[nodes[r]] for r in range(n)]
        right = [0] * n
        for r in range(n):
            j = bisect.bisect_right(val, val[r] + maxDiff, r, n) - 1
            right[r] = j
        LOG = 18
        jump = [[0] * LOG for _ in range(n)]
        for r in range(n):
            jump[r][0] = right[r]
        for b in range(1, LOG):
            for r in range(n):
                jump[r][b] = jump[ jump[r][b-1] ][b-1]
        def reach(start, steps):
            cur = start
            for b in range(LOG - 1, -1, -1):
                if steps & (1 << b):
                    cur = jump[cur][b]
            return cur
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            ru = rank[u]
            rv = rank[v]
            if ru > rv:
                ru, rv = rv, ru
            l, h = 1, n
            min_k = -1
            while l <= h:
                m = (l + h) // 2
                if reach(ru, m) >= rv:
                    min_k = m
                    h = m - 1
                else:
                    l = m + 1
            ans.append(min_k)
        return ans

# @lc code=end