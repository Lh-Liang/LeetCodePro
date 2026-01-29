#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
from bisect import bisect_left
from collections import defaultdict

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # 1. Pre-process: Keep only the best interval for each (l, r) pair
        # Best is defined by max weight, then min original index.
        best_intervals = {}
        for i, (l, r, w) in enumerate(intervals):
            if (l, r) not in best_intervals or w > best_intervals[(l, r)][0] or (w == best_intervals[(l, r)][0] and i < best_intervals[(l, r)][1]):
                best_intervals[(l, r)] = (w, i)
        
        # 2. Sort intervals by end time for DP
        # Each item: (r, l, w, original_index)
        sorted_ints = []
        for (l, r), (w, idx) in best_intervals.items():
            sorted_ints.append((r, l, w, idx))
        sorted_ints.sort()
        
        n = len(sorted_ints)
        ends = [x[0] for x in sorted_ints]
        
        # dp[k][i] = (max_weight, lexicographically_smallest_index_list)
        # We use k=0..4 and i=0..n
        # Initialize with weight 0 and empty index list
        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]
        
        for k in range(1, 5):
            for i in range(1, n + 1):
                r_i, l_i, w_i, idx_i = sorted_ints[i-1]
                
                # Option A: Don't include current interval
                dp[k][i] = dp[k][i-1]
                
                # Option B: Include current interval
                # Find last interval that ends before current starts
                prev_idx = bisect_left(ends, l_i) 
                prev_w, prev_indices = dp[k-1][prev_idx]
                
                curr_w = prev_w + w_i
                curr_indices = sorted(prev_indices + [idx_i])
                
                # Compare with Option A
                if curr_w > dp[k][i][0]:
                    dp[k][i] = (curr_w, curr_indices)
                elif curr_w == dp[k][i][0]:
                    if not dp[k][i][1] or curr_indices < dp[k][i][1]:
                        dp[k][i] = (curr_w, curr_indices)
                        
        return dp[4][n][1]
# @lc code=end