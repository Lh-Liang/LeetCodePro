#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
from typing import List
from collections import defaultdict
from array import array
import sys

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        sys.setrecursionlimit(1_000_000)
        n = len(xCoord)
        pts = list(zip(xCoord, yCoord))

        # Group y's by x (columns)
        cols = defaultdict(list)
        for x, y in pts:
            cols[x].append(y)
        for x in cols:
            cols[x].sort()
        xs_cols = sorted(cols.keys())

        # Coordinate compress y
        yvals = sorted(set(yCoord))
        m = len(yvals)
        y_to_idx = {y: i for i, y in enumerate(yvals)}

        # Sort points by x for persistent structure
        pts_sorted = sorted(((x, y_to_idx[y]) for x, y in pts), key=lambda t: t[0])

        # Persistent segment tree arrays (node 0 is null)
        L = array('I', [0])
        R = array('I', [0])
        S = array('I', [0])

        def update(prev: int, l: int, r: int, pos: int) -> int:
            new = len(S)
            L.append(L[prev])
            R.append(R[prev])
            S.append(S[prev] + 1)
            if l != r:
                mid = (l + r) >> 1
                if pos <= mid:
                    left = update(L[prev], l, mid, pos)
                    L[new] = left
                else:
                    right = update(R[prev], mid + 1, r, pos)
                    R[new] = right
            return new

        def query(node: int, l: int, r: int, ql: int, qr: int) -> int:
            if node == 0 or ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return S[node]
            mid = (l + r) >> 1
            return query(L[node], l, mid, ql, qr) + query(R[node], mid + 1, r, ql, qr)

        # Build roots and x boundary indices:
        # x_to_start[x] = number of points with x < this x
        # x_to_end[x]   = number of points with x <= this x
        roots = [0] * (n + 1)
        x_to_start = {}
        x_to_end = {}

        i = 0
        while i < n:
            x = pts_sorted[i][0]
            start = i
            while i < n and pts_sorted[i][0] == x:
                roots[i + 1] = update(roots[i], 0, m - 1, pts_sorted[i][1])
                i += 1
            end = i
            x_to_start[x] = start
            x_to_end[x] = end

        ans = -1
        last_x_for_pair = {}

        for x2 in xs_cols:
            ys = cols[x2]
            for j in range(len(ys) - 1):
                y1 = ys[j]
                y2 = ys[j + 1]
                key = (y1 << 32) | y2

                if key in last_x_for_pair:
                    x1 = last_x_for_pair[key]
                    area = (x2 - x1) * (y2 - y1)
                    if area > ans:
                        # Count points in closed rectangle [x1,x2] x [y1,y2]
                        idxL = x_to_start[x1]   # x < x1
                        idxR = x_to_end[x2]     # x <= x2
                        yl = y_to_idx[y1]
                        yr = y_to_idx[y2]
                        cnt = query(roots[idxR], 0, m - 1, yl, yr) - query(roots[idxL], 0, m - 1, yl, yr)
                        if cnt == 4:
                            ans = area

                last_x_for_pair[key] = x2

        return ans
# @lc code=end
