#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#

from typing import List

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        rem = [x % k for x in nums]
        b = [x // k for x in nums]

        # ---------- Sparse Table for range min/max on rem ----------
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1
        K = lg[n] + 1

        st_min = [rem[:]]
        st_max = [rem[:]]
        j = 1
        while (1 << j) <= n:
            prev_min = st_min[j - 1]
            prev_max = st_max[j - 1]
            length = 1 << j
            half = length >> 1
            cur_min = [0] * (n - length + 1)
            cur_max = [0] * (n - length + 1)
            for i in range(n - length + 1):
                cur_min[i] = min(prev_min[i], prev_min[i + half])
                cur_max[i] = max(prev_max[i], prev_max[i + half])
            st_min.append(cur_min)
            st_max.append(cur_max)
            j += 1

        def range_min_max(l: int, r: int) -> (int, int):
            length = r - l + 1
            j = lg[length]
            p = 1 << j
            mn = min(st_min[j][l], st_min[j][r - p + 1])
            mx = max(st_max[j][l], st_max[j][r - p + 1])
            return mn, mx

        # ---------- Persistent Segment Tree over values of b ----------
        vals = sorted(set(b))
        m = len(vals)
        idx_map = {v: i for i, v in enumerate(vals)}

        lch = [0]
        rch = [0]
        cnt = [0]
        sm = [0]

        def new_node(L: int, R: int, C: int, S: int) -> int:
            lch.append(L)
            rch.append(R)
            cnt.append(C)
            sm.append(S)
            return len(cnt) - 1

        def update(prev: int, tl: int, tr: int, pos: int, addv: int) -> int:
            node = new_node(lch[prev], rch[prev], cnt[prev] + 1, sm[prev] + addv)
            if tl != tr:
                tm = (tl + tr) // 2
                if pos <= tm:
                    nl = update(lch[prev], tl, tm, pos, addv)
                    lch[node] = nl
                else:
                    nr = update(rch[prev], tm + 1, tr, pos, addv)
                    rch[node] = nr
            return node

        roots = [0] * (n + 1)
        for i in range(n):
            p = idx_map[b[i]]
            roots[i + 1] = update(roots[i], 0, m - 1, p, b[i])

        def kth(nodeR: int, nodeL: int, tl: int, tr: int, ksmall: int) -> int:
            if tl == tr:
                return tl
            leftR = lch[nodeR]
            leftL = lch[nodeL]
            leftCount = cnt[leftR] - cnt[leftL]
            tm = (tl + tr) // 2
            if ksmall <= leftCount:
                return kth(leftR, leftL, tl, tm, ksmall)
            return kth(rch[nodeR], rch[nodeL], tm + 1, tr, ksmall - leftCount)

        def query(nodeR: int, nodeL: int, tl: int, tr: int, ql: int, qr: int) -> (int, int):
            if qr < tl or tr < ql:
                return 0, 0
            if ql <= tl and tr <= qr:
                return cnt[nodeR] - cnt[nodeL], sm[nodeR] - sm[nodeL]
            tm = (tl + tr) // 2
            c1, s1 = query(lch[nodeR], lch[nodeL], tl, tm, ql, qr)
            c2, s2 = query(rch[nodeR], rch[nodeL], tm + 1, tr, ql, qr)
            return c1 + c2, s1 + s2

        ans = []
        for l, r in queries:
            if l == r:
                ans.append(0)
                continue

            mn, mx = range_min_max(l, r)
            if mn != mx:
                ans.append(-1)
                continue

            rootR = roots[r + 1]
            rootL = roots[l]
            length = r - l + 1

            # lower median
            ksmall = (length + 1) // 2
            pos = kth(rootR, rootL, 0, m - 1, ksmall)
            med = vals[pos]

            leftCnt, leftSum = query(rootR, rootL, 0, m - 1, 0, pos)
            totalSum = sm[rootR] - sm[rootL]
            rightCnt = length - leftCnt
            rightSum = totalSum - leftSum

            cost = med * leftCnt - leftSum + rightSum - med * rightCnt
            ans.append(cost)

        return ans
# @lc code=end
