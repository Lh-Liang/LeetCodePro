#
# @lc app=leetcode id=3488 lang=python3
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
from typing import List
import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from collections import defaultdict
        n = len(nums)
        value_indices = defaultdict(list)
        for i, val in enumerate(nums):
            value_indices[val].append(i)
        
        result = []
        for qidx in queries:
            val = nums[qidx]
            indices = value_indices[val]
            if len(indices) == 1:
                result.append(-1)
                continue
            # Binary search to find insertion point
            idx = bisect.bisect_left(indices, qidx)
            # Find the closest neighbor
            # Consider both circular directions
            prev_idx = indices[idx - 1] if idx > 0 else indices[-1]
            next_idx = indices[idx] if idx < len(indices) and indices[idx] != qidx else (indices[0] if indices[0] != qidx else indices[1])
            dist1 = (qidx - prev_idx) % n if prev_idx != qidx else n
            dist2 = (next_idx - qidx) % n if next_idx != qidx else n
            min_dist = min(dist1, dist2)
            result.append(min_dist)
        return result
# @lc code=end