#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#
# @lc code=start
from typing import List
import math

class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 2)

    def update(self, index: int, delta: int) -> None:
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        mods = [num % k for num in nums]
        qarr = [num // k for num in nums]

        # Sparse table for range min/max on mods
        LOG = n.bit_length()
        st_min = [[0] * n for _ in range(LOG)]
        st_max = [[0] * n for _ in range(LOG)]
        for i in range(n):
            st_min[0][i] = mods[i]
            st_max[0][i] = mods[i]
        for j in range(1, LOG):
            for i in range(n - (1 << j) + 1):
                st_min[j][i] = min(st_min[j-1][i], st_min[j-1][i + (1 << (j-1))])
                st_max[j][i] = max(st_max[j-1][i], st_max[j-1][i + (1 << (j-1))])

        def get_log(length: int) -> int:
            j = 0
            while (1 << (j + 1)) <= length:
                j += 1
            return j

        def range_min(l: int, r: int) -> int:
            length = r - l + 1
            j = get_log(length)
            return min(st_min[j][l], st_min[j][r - (1 << j) + 1])

        def range_max(l: int, r: int) -> int:
            length = r - l + 1
            j = get_log(length)
            return max(st_max[j][l], st_max[j][r - (1 << j) + 1])

        # Mo's algorithm setup
        B = int(math.sqrt(n)) + 1
        query_list = [[l, r, i] for i, (l, r) in enumerate(queries)]
        query_list.sort(key=lambda x: (x[0] // B, x[1]))

        # Coordinate compression
        vals = sorted(set(qarr))
        m = len(vals)
        ranks = {vals[i]: i + 1 for i in range(m)}

        mo_ans = [0] * len(queries)
        ft_count = FenwickTree(m)
        ft_sumval = FenwickTree(m)
        cur_l = 0
        cur_r = -1

        def add(pos: int):
            rk = ranks[qarr[pos]]
            ft_count.update(rk, 1)
            ft_sumval.update(rk, qarr[pos])

        def remove(pos: int):
            rk = ranks[qarr[pos]]
            ft_count.update(rk, -1)
            ft_sumval.update(rk, -qarr[pos])

        for ql, qr, qidx in query_list:
            while cur_r < qr:
                cur_r += 1
                add(cur_r)
            while cur_l > ql:
                cur_l -= 1
                add(cur_l)
            while cur_r > qr:
                remove(cur_r)
                cur_r -= 1
            while cur_l < ql:
                remove(cur_l)
                cur_l += 1
            sz = cur_r - cur_l + 1
            need = sz // 2 + 1
            # Binary search for med_rk
            lo, hi = 1, m
            while lo < hi:
                md = (lo + hi) // 2
                if ft_count.query(md) >= need:
                    hi = md
                else:
                    lo = md + 1
            med_rk = lo
            med = vals[med_rk - 1]
            num_lt = ft_count.query(med_rk - 1) if med_rk > 1 else 0
            cnt_ge = sz - num_lt
            total_sumq = ft_sumval.query(m)
            sum_lt = ft_sumval.query(med_rk - 1) if med_rk > 1 else 0
            sum_ge = total_sumq - sum_lt
            mo_ans[qidx] = (2 * sum_ge - total_sumq) - med * (2 * cnt_ge - sz)

        # Build final ans
        ans = []
        for i, (l, r) in enumerate(queries):
            if range_min(l, r) != range_max(l, r):
                ans.append(-1)
            else:
                ans.append(mo_ans[i])
        return ans

# @lc code=end