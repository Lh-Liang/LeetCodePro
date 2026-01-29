#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # 1. Aggressive Pruning: For unique [l, r], keep only max weight and min index.
        best_intervals = {}
        for i, (l, r, w) in enumerate(intervals):
            if (l, r) not in best_intervals:
                best_intervals[(l, r)] = (w, i)
            else:
                curr_w, curr_idx = best_intervals[(l, r)]
                if w > curr_w or (w == curr_w and i < curr_idx):
                    best_intervals[(l, r)] = (w, i)
        
        # 2. Prepare sorted intervals for DP
        # ivs: (l, r, w, original_index)
        ivs = sorted([(l, r, w, idx) for (l, r), (w, idx) in best_intervals.items()])
        n = len(ivs)
        starts = [x[0] for x in ivs]
        
        # Pre-calculate next valid index: first j where ivs[j].l > ivs[i].r
        next_j = [bisect.bisect_right(starts, ivs[i][1]) for i in range(n)]
        
        # dp[i] stores (max_weight, tuple_of_indices) for the current k
        # Using suffix DP to find best selection from [i...n-1]
        prev_dp = [(0, ())] * (n + 1)
        
        for k in range(1, 5):
            curr_dp = [(0, ())] * (n + 1)
            for i in range(n - 1, -1, -1):
                # Option 1: Skip interval i
                best_w, best_idx = curr_dp[i+1]
                
                # Option 2: Take interval i
                w_i = ivs[i][2]
                idx_i = ivs[i][3]
                w_next, idx_next = prev_dp[next_j[i]]
                
                new_w = w_i + w_next
                # To maintain lexicographical order, we need indices sorted.
                # Since we process intervals by start time, we can merge idx_i with idx_next.
                # However, the problem asks for the smallest array of indices.
                new_indices = tuple(sorted(idx_next + (idx_i,)))
                
                if new_w > best_w:
                    best_w, best_idx = new_w, new_indices
                elif new_w == best_w:
                    if not best_idx or new_indices < best_idx:
                        best_idx = new_indices
                
                curr_dp[i] = (best_w, best_idx)
            prev_dp = curr_dp
            
        return list(prev_dp[0][1])
# @lc code=end