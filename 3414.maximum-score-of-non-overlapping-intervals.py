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
        # Store as (l, r, w, original_index)
        n = len(intervals)
        arr = []
        for i in range(n):
            arr.append((intervals[i][0], intervals[i][1], intervals[i][2], i))
        
        # Sort by start time to use suffix DP
        arr.sort()
        starts = [x[0] for x in arr]
        
        # dp[k][i] = (max_weight, lexicographically_smallest_tuple_of_indices)
        # We use k from 1 to 4 and i from n down to 0
        # Using a 1D DP for space optimization (prev_dp for k-1, curr_dp for k)
        prev_dp = [(0, ())] * (n + 1)
        
        # Final answer tracker
        best_total_weight = 0
        best_indices = ()

        for k in range(1, 5):
            curr_dp = [(0, ())] * (n + 1)
            for i in range(n - 1, -1, -1):
                l, r, w, idx = arr[i]
                
                # Option 1: Skip current interval
                res_w, res_idx = curr_dp[i+1]
                
                # Option 2: Take current interval
                # Find first interval starting after current ends
                next_idx = bisect_left(starts, r + 1)
                take_w, take_idx = prev_dp[next_idx]
                new_w = w + take_w
                new_idx = tuple(sorted((idx,) + take_idx))
                
                # Compare weight then lexicographical order
                if new_w > res_w:
                    res_w, res_idx = new_w, new_idx
                elif new_w == res_w:
                    if not res_idx or new_idx < res_idx:
                        res_idx = new_idx
                
                curr_dp[i] = (res_w, res_idx)
            
            # Update global best
            w_k, idx_k = curr_dp[0]
            if w_k > best_total_weight:
                best_total_weight = w_k
                best_indices = idx_k
            elif w_k == best_total_weight and w_k > 0:
                if not best_indices or idx_k < best_indices:
                    best_indices = idx_k
            
            prev_dp = curr_dp
            
        return list(best_indices)
# @lc code=end