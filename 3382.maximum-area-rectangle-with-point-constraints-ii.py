#
# @lc app=leetcode id=3382 lang=python3
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
from typing import List
from collections import defaultdict
import bisect

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        n = len(xCoord)
        if n < 4:
            return -1
        x_to_ys = defaultdict(list)
        for i in range(n):
            x_to_ys[xCoord[i]].append(yCoord[i])
        X = sorted(x_to_ys.keys())
        mx = len(X)
        if mx < 2:
            return -1
        x_to_rank = {X[i]: i + 1 for i in range(mx)}
        for x in list(x_to_ys.keys()):
            x_to_ys[x].sort()
        supports = defaultdict(list)
        for x, ys in x_to_ys.items():
            if len(ys) < 2:
                continue
            for j in range(len(ys) - 1):
                yb = ys[j]
                yt = ys[j + 1]
                supports[(yb, yt)].append(x)
        all_y = set()
        for ys in x_to_ys.values():
            all_y.update(ys)
        Y = sorted(all_y)
        my = len(Y)
        y_to_rank = {Y[i]: i + 1 for i in range(my)}
        xrank_to_yranks = [[] for _ in range(mx + 1)]
        for x, ys in x_to_ys.items():
            r = x_to_rank[x]
            for yv in ys:
                xrank_to_yranks[r].append(y_to_rank[yv])
        tree = [[] for _ in range(4 * (mx + 1))]
        def build(node: int, start: int, end: int) -> None:
            if start == end:
                tree[node] = xrank_to_yranks[start][:]
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            left = tree[2 * node]
            right = tree[2 * node + 1]
            i = j = 0
            merged = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            tree[node] = merged
        build(1, 1, mx)
        def has_point(xlo: int, xhi: int, ylo: int, yhi: int) -> bool:
            if xlo > xhi:
                return False
            def query(node: int, nstart: int, nend: int, qstart: int, qend: int) -> bool:
                if qstart > nend or qend < nstart:
                    return False
                if qstart <= nstart and nend <= qend:
                    lst = tree[node]
                    if not lst:
                        return False
                    idx = bisect.bisect_left(lst, ylo)
                    return idx < len(lst) and lst[idx] <= yhi
                mid = (nstart + nend) // 2
                if query(2 * node, nstart, mid, qstart, qend):
                    return True
                return query(2 * node + 1, mid + 1, nend, qstart, qend)
            return query(1, 1, mx, xlo, xhi)
        max_area = 0
        for (yb, yt), xlist in supports.items():
            slist = sorted(set(xlist))
            if len(slist) < 2:
                continue
            ylo = y_to_rank[yb]
            yhi = y_to_rank[yt]
            for k in range(len(slist) - 1):
                xl_val = slist[k]
                xr_val = slist[k + 1]
                xl_r = x_to_rank[xl_val]
                xr_r = x_to_rank[xr_val]
                if not has_point(xl_r + 1, xr_r - 1, ylo, yhi):
                    area = (xr_val - xl_val) * (yt - yb)
                    if area > max_area:
                        max_area = area
        return max_area if max_area > 0 else -1

# @lc code=end