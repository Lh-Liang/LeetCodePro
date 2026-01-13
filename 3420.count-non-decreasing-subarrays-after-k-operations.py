#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
from typing import List
from bisect import bisect_right


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        NEG_INF = -10**20

        class Window:
            __slots__ = (
                "front", "fp", "front_ps", "front_smax", "front_fmax",
                "back", "back_sum",
                "seg_vals", "pref_cnt", "pref_wsum",
            )

            def __init__(self):
                # front part: array + pointer
                self.front = []
                self.fp = 0
                self.front_ps = []
                self.front_smax = []
                self.front_fmax = []

                # back part: dynamic array + segment summary
                self.back = []
                self.back_sum = 0
                self.seg_vals = []      # increasing
                self.pref_cnt = []      # prefix counts of elements
                self.pref_wsum = []     # prefix sums of (seg_val * seg_count)

            def __len__(self) -> int:
                return (len(self.front) - self.fp) + len(self.back)

            def _rebuild_front_from_back(self) -> None:
                # Move all back elements to front (in order), clear back.
                self.front = self.back
                self.fp = 0
                self.back = []
                self.back_sum = 0
                self.seg_vals = []
                self.pref_cnt = []
                self.pref_wsum = []

                F = self.front
                m = len(F)
                if m == 0:
                    self.front_ps = []
                    self.front_smax = []
                    self.front_fmax = []
                    return

                # prefix sums of values
                ps = [0] * (m + 1)
                for i, x in enumerate(F):
                    ps[i + 1] = ps[i] + x

                # next greater to the right (strict)
                ng = [-1] * m
                st = []
                for i in range(m - 1, -1, -1):
                    x = F[i]
                    while st and F[st[-1]] <= x:
                        st.pop()
                    ng[i] = st[-1] if st else -1
                    st.append(i)

                # DP for sum of running maxima and final max
                smax = [0] * m
                fmax = [0] * m
                for i in range(m - 1, -1, -1):
                    j = ng[i]
                    if j == -1:
                        smax[i] = F[i] * (m - i)
                        fmax[i] = F[i]
                    else:
                        smax[i] = F[i] * (j - i) + smax[j]
                        fmax[i] = fmax[j]

                self.front_ps = ps
                self.front_smax = smax
                self.front_fmax = fmax

            def push_right(self, x: int) -> None:
                self.back.append(x)
                self.back_sum += x

                if not self.seg_vals:
                    self.seg_vals.append(x)
                    self.pref_cnt.append(1)
                    self.pref_wsum.append(x)
                    return

                if x > self.seg_vals[-1]:
                    self.seg_vals.append(x)
                    self.pref_cnt.append(self.pref_cnt[-1] + 1)
                    self.pref_wsum.append(self.pref_wsum[-1] + x)
                else:
                    # prefix maximum stays seg_vals[-1]
                    self.pref_cnt[-1] += 1
                    self.pref_wsum[-1] += self.seg_vals[-1]

            def pop_left(self) -> None:
                if self.fp < len(self.front):
                    self.fp += 1
                    return
                # front empty; rebuild from back
                if not self.back:
                    return
                self._rebuild_front_from_back()
                # pop one
                self.fp += 1

            def _front_sum(self) -> int:
                if self.fp >= len(self.front):
                    return 0
                return self.front_ps[-1] - self.front_ps[self.fp]

            def _front_smax(self) -> int:
                if self.fp >= len(self.front):
                    return 0
                return self.front_smax[self.fp]

            def _front_fmax(self) -> int:
                if self.fp >= len(self.front):
                    return NEG_INF
                return self.front_fmax[self.fp]

            def _back_summax_with_initial(self, M: int) -> int:
                # Sum over back positions of max(M, backPrefixMax[i])
                if not self.seg_vals:
                    return 0
                idx = bisect_right(self.seg_vals, M)  # number of seg_vals <= M
                total_w = self.pref_wsum[-1]
                if idx == 0:
                    return total_w
                w_le = self.pref_wsum[idx - 1]
                c_le = self.pref_cnt[idx - 1]
                return M * c_le + (total_w - w_le)

            def cost(self) -> int:
                sum_runmax_front = self._front_smax()
                M = self._front_fmax()
                sum_runmax_back = self._back_summax_with_initial(M)
                sum_nums = self._front_sum() + self.back_sum
                return (sum_runmax_front + sum_runmax_back) - sum_nums

        w = Window()
        ans = 0

        for x in nums:
            w.push_right(x)
            while len(w) > 0 and w.cost() > k:
                w.pop_left()
            ans += len(w)

        return ans
# @lc code=end
