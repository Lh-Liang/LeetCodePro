#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

from typing import List
import bisect

# @lc code=start
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        if n == 0:
            return []
        
        inter = [(intervals[j][0], intervals[j][1], intervals[j][2], j) for j in range(n)]
        sorted_inter = sorted(inter, key=lambda x: x[1])
        ends = [x[1] for x in sorted_inter]
        
        INF = float('-inf')
        score_dp = [[INF] * 5 for _ in range(n + 1)]
        list_dp = [[[] for _ in range(5)] for _ in range(n + 1)]
        score_dp[0][0] = 0
        
        for i in range(1, n + 1):
            this_start, this_end, this_w, this_idx = sorted_inter[i - 1]
            for k in range(5):
                # Not take
                score_dp[i][k] = score_dp[i - 1][k]
                list_dp[i][k] = list_dp[i - 1][k][:]
                
                # Take
                if k >= 1:
                    pos = bisect.bisect_left(ends, this_start, 0, i)
                    prev_j = pos - 1
                    prev_m = prev_j + 1 if prev_j >= 0 else 0
                    prev_s = score_dp[prev_m][k - 1]
                    if prev_s != INF:
                        new_s = prev_s + this_w
                        prev_l = list_dp[prev_m][k - 1]
                        new_l = sorted(prev_l + [this_idx])
                        
                        curr_s = score_dp[i][k]
                        curr_l = list_dp[i][k]
                        
                        update = False
                        if new_s > curr_s:
                            update = True
                        elif new_s == curr_s:
                            if new_l < curr_l:
                                update = True
                        
                        if update:
                            score_dp[i][k] = new_s
                            list_dp[i][k] = new_l
        
        max_s = max(score_dp[n][k] for k in range(5))
        best_lists = [list_dp[n][k] for k in range(5) if score_dp[n][k] == max_s]
        return min(best_lists)

# @lc code=end
