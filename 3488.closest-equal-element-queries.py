#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
from collections import defaultdict
import bisect
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)
        for i in range(n):
            pos[nums[i]].append(i)
        ans = []
        for q in queries:
            positions = pos[nums[q]]
            m = len(positions)
            if m <= 1:
                ans.append(-1)
                continue
            idx = bisect.bisect_left(positions, q)
            pidx = (idx - 1 + m) % m
            nidx = (idx + 1) % m
            prev = positions[pidx]
            nxt = positions[nidx]
            d1 = min(abs(q - prev), n - abs(q - prev))
            d2 = min(abs(q - nxt), n - abs(q - nxt))
            ans.append(min(d1, d2))
        return ans
# @lc code=end