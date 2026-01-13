#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

from typing import List

# @lc code=start
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        def tri(x: int) -> int:
            return x * (x + 1) // 2

        # Build maximal non-decreasing runs
        starts: List[int] = []
        ends: List[int] = []
        contrib: List[int] = []
        runId = [-1] * n

        s = 0
        rid = 0
        for i in range(n - 1):
            if nums[i] <= nums[i + 1]:
                continue
            # close run [s, i]
            starts.append(s)
            ends.append(i)
            L = i - s + 1
            contrib.append(tri(L))
            for k in range(s, i + 1):
                runId[k] = rid
            rid += 1
            s = i + 1

        # close last run [s, n-1]
        starts.append(s)
        ends.append(n - 1)
        L = (n - 1) - s + 1
        contrib.append(tri(L))
        for k in range(s, n):
            runId[k] = rid
        rid += 1

        m = rid  # number of runs

        # Prefix sums of full run contributions
        pref = [0] * (m + 1)
        for i in range(m):
            pref[i + 1] = pref[i] + contrib[i]

        ans: List[int] = []
        for l, r in queries:
            i = runId[l]
            j = runId[r]
            if i == j:
                ans.append(tri(r - l + 1))
            else:
                left_len = ends[i] - l + 1
                right_len = r - starts[j] + 1
                mid = pref[j] - pref[i + 1]  # full runs between i and j
                ans.append(tri(left_len) + tri(right_len) + mid)

        return ans
# @lc code=end
