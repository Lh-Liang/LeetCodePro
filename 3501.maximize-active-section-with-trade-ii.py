#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
from typing import List

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (4 * n + 4)

    def update(self, idx: int, val: int):
        idx += self.n
        self.tree[idx] = val
        idx //= 2
        while idx >= 1:
            self.tree[idx] = max(self.tree[2 * idx], self.tree[2 * idx + 1])
            idx //= 2

    def query(self, left: int, right: int) -> int:
        if left > right:
            return 0
        res = 0
        left += self.n
        right += self.n + 1
        while left < right:
            if left & 1:
                res = max(res, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                res = max(res, self.tree[right])
            left >>= 1
            right >>= 1
        return res

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        if n == 0:
            return [0] * len(queries)
        # total ones
        total_ones = sum(1 for c in s if c == '1')
        # 1-runs: list of (start, end)
        one_runs = []
        i = 0
        while i < n:
            if s[i] == '1':
                start = i
                while i < n and s[i] == '1':
                    i += 1
                end = i - 1
                one_runs.append((start, end))
            else:
                i += 1
        num_runs = len(one_runs)
        if num_runs == 0:
            return [total_ones] * len(queries)
        # arrays
        start_arr = [0] * num_runs
        end_arr = [0] * num_runs
        left0_start_arr = [0] * num_runs
        right0_end_arr = [0] * num_runs
        lb_arr = [0] * num_runs
        global_gain_arr = [0] * num_runs
        candidates = []
        lb_to_gain = {}
        for k in range(num_runs):
            start_arr[k], end_arr[k] = one_runs[k]
            lb_arr[k] = start_arr[k] - 1
            prev_end = -1 if k == 0 else end_arr[k - 1]
            left0_start_arr[k] = prev_end + 1
            bl = start_arr[k] - left0_start_arr[k]
            next_start = n if k == num_runs - 1 else start_arr[k + 1]
            right0_end_arr[k] = next_start - 1
            br = right0_end_arr[k] - end_arr[k]
            if bl >= 1 and br >= 1:
                gain = bl + br
                global_gain_arr[k] = gain
                rb = end_arr[k] + 1
                lb_to_gain[lb_arr[k]] = gain
                candidates.append((rb, lb_arr[k], gain))
        # special arrays
        next_one_after_zero = [-1] * n
        prev_one_before_zero = [-1] * n
        for k in range(num_runs):
            # left 0-run
            ls = left0_start_arr[k]
            le = start_arr[k] - 1
            if 0 <= ls <= le < n:
                for p in range(ls, le + 1):
                    next_one_after_zero[p] = k
            # right 0-run
            rs = end_arr[k] + 1
            re = right0_end_arr[k]
            if 0 <= rs <= re < n:
                for p in range(rs, re + 1):
                    prev_one_before_zero[p] = k
        # sort candidates by rb
        candidates.sort()
        m = len(candidates)
        # queries offline
        q = len(queries)
        qlist = [None] * q
        for idx in range(q):
            li, ri = queries[idx]
            qlist[idx] = (ri, li, idx)
        qlist.sort()
        # segtree
        st = SegmentTree(n)
        ptr = 0
        ans = [0] * q
        for rq_r, rq_l, qidx in qlist:
            while ptr < m and candidates[ptr][0] <= rq_r:
                _, lb, gn = candidates[ptr]
                st.update(lb, gn)
                ptr += 1
            # specials
            special_ks = set()
            if rq_l < n and s[rq_l] == '0':
                k = next_one_after_zero[rq_l]
                if k != -1:
                    stt = start_arr[k]
                    en = end_arr[k]
                    if rq_l < stt and en < rq_r:
                        special_ks.add(k)
            if rq_r > rq_l and rq_r < n and s[rq_r] == '0':
                k = prev_one_before_zero[rq_r]
                if k != -1:
                    stt = start_arr[k]
                    en = end_arr[k]
                    if rq_l < stt and en < rq_r:
                        special_ks.add(k)
            # lbs to exclude
            lbs_to_exclude = []
            for k in special_ks:
                lb = lb_arr[k]
                if lb >= rq_l and lb in lb_to_gain:  # valid candidate
                    lbs_to_exclude.append(lb)
            # temp zero
            for lb in lbs_to_exclude:
                st.update(lb, 0)
            max_non = st.query(rq_l, n - 1)
            # restore
            for lb in lbs_to_exclude:
                st.update(lb, lb_to_gain[lb])
            # special actuals
            max_spec = 0
            for k in special_ks:
                l0s = left0_start_arr[k]
                r0e = right0_end_arr[k]
                blc = start_arr[k] - max(rq_l, l0s)
                brc = min(rq_r, r0e) - end_arr[k]
                act = blc + brc
                max_spec = max(max_spec, act)
            # overall
            this_gain = max(max_non, max_spec)
            ans[qidx] = total_ones + this_gain
        return ans

# @lc code=end