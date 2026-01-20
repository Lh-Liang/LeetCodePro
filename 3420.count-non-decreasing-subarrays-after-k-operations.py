#
# @lc app=leetcode id=3420 lang=python3
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#
# @lc code=start
import typing
class Solution:
    def countNonDecreasingSubarrays(self, nums: typing.List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # precompute log
        logs = [0] * (n + 1)
        for i in range(2, n + 1):
            logs[i] = logs[i // 2] + 1

        # sparse table for leftmost max index
        LOG = 18
        st = [[0] * n for _ in range(LOG)]
        for i in range(n):
            st[0][i] = i
        for kk in range(1, LOG):
            for i in range(n - (1 << kk) + 1):
                i2 = i + (1 << (kk - 1))
                idx1 = st[kk - 1][i]
                idx2 = st[kk - 1][i2]
                if nums[idx1] >= nums[idx2]:
                    st[kk][i] = idx1
                else:
                    st[kk][i] = idx2

        def query(L: int, R: int) -> int:
            length = R - L + 1
            kk = logs[length]
            idx1 = st[kk][L]
            idx2 = st[kk][R - (1 << kk) + 1]
            if nums[idx1] >= nums[idx2]:
                return idx1
            else:
                return idx2

        def get_cost(l: int, r: int) -> int:
            if l >= r:
                return 0
            res = 0
            while l < r:
                s = query(l, r)
                lift = (r - s) * nums[s] - (pref[r + 1] - pref[s + 1])
                res += lift
                r = s - 1
            return res

        ans = 0
        for rr in range(n):
            # binary search minimal l0 s.t. get_cost(l0, rr) <= k
            lo = 0
            hi = rr
            while lo < hi:
                mid = (lo + hi) // 2
                if get_cost(mid, rr) <= k:
                    hi = mid
                else:
                    lo = mid + 1
            if get_cost(lo, rr) <= k:
                ans += rr - lo + 1
        return ans
# @lc code=end