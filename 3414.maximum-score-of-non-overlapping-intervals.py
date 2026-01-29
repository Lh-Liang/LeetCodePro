#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store as (start, end, weight, original_index)
        # Sorting by start time is necessary for the suffix DP and binary search logic.
        sorted_ints = sorted((intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n))
        
        starts = [x[0] for x in sorted_ints]
        weights = [x[2] for x in sorted_ints]
        ids = [x[3] for x in sorted_ints]
        
        # Precompute the index of the first interval that starts after each interval i ends.
        # Intervals are non-overlapping if l_next > r_current.
        nxt = [bisect_left(starts, sorted_ints[i][1] + 1) for i in range(n)]
            
        # dp_w stores the maximum weight for up to k intervals.
        # dp_idx stores the best set of indices as a negated tuple.
        # We use a flat list for performance; size is (n + 1) * 5.
        dp_w = [0] * ((n + 1) * 5)
        dp_idx = [()] * ((n + 1) * 5)
        
        # Process intervals from right to left (suffix DP).
        for i in range(n - 1, -1, -1):
            w = weights[i]
            neg_idx = -ids[i]
            ni = nxt[i]
            
            cur_off = i * 5
            nxt_off = (i + 1) * 5
            ni_off = ni * 5
            
            for k in range(1, 5):
                # Option 1: Skip the current interval.
                skip_w = dp_w[nxt_off + k]
                skip_idx = dp_idx[nxt_off + k]
                
                # Option 2: Include the current interval.
                take_w = w + dp_w[ni_off + k - 1]
                # Maintain the indices in a sorted, negated tuple.
                # Negated comparison: (-1, -3) > (-2) means [1, 3] is lexicographically smaller than [2].
                take_idx = tuple(sorted(dp_idx[ni_off + k - 1] + (neg_idx,), reverse=True))
                
                # Compare weight first, then use the negated tuple for lexicographical tie-breaking.
                if take_w > skip_w or (take_w == skip_w and take_idx > skip_idx):
                    dp_w[cur_off + k] = take_w
                    dp_idx[cur_off + k] = take_idx
                else:
                    dp_w[cur_off + k] = skip_w
                    dp_idx[cur_off + k] = skip_idx
                        
        # The result for the whole array with up to 4 intervals is at dp[0][4].
        final_neg_indices = dp_idx[4]
        return sorted([-x for x in final_neg_indices])
# @lc code=end