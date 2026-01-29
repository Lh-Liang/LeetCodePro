# @lc app=leetcode id=3414 lang=python3
# [3414] Maximum Score of Non-overlapping Intervals

# @lc code=start
from typing import List
import bisect

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Sort intervals based on their end times, and then by start times if tied on end times.
        # This helps in considering them in order of appearance with priority on non-overlapping.
        intervals.sort(key=lambda x: (x[1], x[0]))
        
        n = len(intervals)
        dp = [0] * n  # dp[i] will store max score up to interval i
        selected_intervals = [[] for _ in range(n)]  # Track indices for lexicographical smallest result
        
        # Function to find last non-overlapping interval using binary search
        def find_last_non_overlapping(i):
            lo, hi = 0, i - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if intervals[mid][1] < intervals[i][0]:
                    if intervals[mid + 1][1] < intervals[i][0]:
                        lo = mid + 1
                    else:
                        return mid
                else:
                    hi = mid - 1
            return -1

        for i in range(n):
            # Option 1: Take this interval i alone (if no valid previous)
            last_index = find_last_non_overlapping(i)
            current_weight = intervals[i][2]
            if last_index != -1:
                current_weight += dp[last_index]
            
            # Option 2: Skip this interval and take previous best only (dp[i-1])
            if i > 0:
                if dp[i - 1] > current_weight:
                    dp[i] = dp[i - 1]
                    selected_intervals[i] = selected_intervals[i - 1].copy()
                else:
                    dp[i] = current_weight
                    selected_intervals[i] = selected_intervals[last_index].copy() if last_index != -1 else []
                    selected_intervals[i].append(i)
            else:
                dp[i] = current_weight
                selected_intervals[i].append(i)
            
        max_score_index = max(range(n), key=lambda i: dp[i])
        return sorted(selected_intervals[max_score_index])[:4]
# @lc code=end