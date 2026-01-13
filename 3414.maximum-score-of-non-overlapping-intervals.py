#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Create list of (start, end, weight, original_index)
        indexed_intervals = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        
        # Sort by end time for efficient processing
        indexed_intervals.sort(key=lambda x: x[1])
        
        # dp[i][k] = (max_weight, indices_list) 
        # considering first i intervals (in sorted order), selecting exactly k
        dp = [[None for _ in range(5)] for _ in range(n + 1)]
        dp[0][0] = (0, [])
        
        for i in range(n):
            start, end, weight, orig_idx = indexed_intervals[i]
            
            # Option 1: Don't take current interval
            for k in range(5):
                if dp[i][k] is not None:
                    curr_weight, curr_indices = dp[i][k]
                    if dp[i+1][k] is None or dp[i+1][k][0] < curr_weight:
                        dp[i+1][k] = (curr_weight, curr_indices[:])
                    elif dp[i+1][k][0] == curr_weight and curr_indices < dp[i+1][k][1]:
                        dp[i+1][k] = (curr_weight, curr_indices[:])
            
            # Option 2: Take current interval (if we haven't selected 4 yet)
            for k in range(4):
                if dp[i][k] is not None:
                    curr_weight, curr_indices = dp[i][k]
                    
                    # Check if current interval doesn't overlap with already selected ones
                    can_take = True
                    for prev_orig_idx in curr_indices:
                        prev_start, prev_end, prev_weight = intervals[prev_orig_idx]
                        # Two intervals are non-overlapping if one ends before the other starts
                        if not (prev_end < start or end < prev_start):
                            can_take = False
                            break
                    
                    if can_take:
                        new_weight = curr_weight + weight
                        new_indices = sorted(curr_indices + [orig_idx])
                        
                        if dp[i+1][k+1] is None or dp[i+1][k+1][0] < new_weight:
                            dp[i+1][k+1] = (new_weight, new_indices)
                        elif dp[i+1][k+1][0] == new_weight and new_indices < dp[i+1][k+1][1]:
                            dp[i+1][k+1] = (new_weight, new_indices)
        
        # Find the result: maximum weight with lexicographically smallest indices
        max_weight = 0
        result = []
        for k in range(5):
            if dp[n][k] is not None:
                weight, indices = dp[n][k]
                if weight > max_weight:
                    max_weight = weight
                    result = indices
                elif weight == max_weight and indices < result:
                    result = indices
        
        return result
# @lc code=end