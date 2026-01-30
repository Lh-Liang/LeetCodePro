#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
from typing import List
import bisect

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Attach original indices
        intervals_with_idx = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)], key=lambda x: (x[1], x[0], x[2], x[3]))
        # Prepare for binary search: sorted by end time
        ends = [interval[1] for interval in intervals_with_idx]

        # dp[k][i] = (score, indices list) for best up to i, using k intervals
        dp = [ [(0, []) for _ in range(n+1)] for _ in range(5) ]
        for i in range(1, n+1):
            l, r, w, idx = intervals_with_idx[i-1]
            for k in range(1, 5):
                # Option 1: Don't take this interval
                if dp[k][i-1][0] > dp[k][i][0] or (dp[k][i-1][0] == dp[k][i][0] and dp[k][i-1][1] < dp[k][i][1]):
                    dp[k][i] = dp[k][i-1]
                # Option 2: Take this interval
                # Find last non-overlapping interval
                j = bisect.bisect_right(ends, l-1, 0, i-1)
                cand_score = dp[k-1][j][0] + w
                cand_indices = dp[k-1][j][1] + [idx]
                if (cand_score > dp[k][i][0] or 
                    (cand_score == dp[k][i][0] and sorted(cand_indices) < sorted(dp[k][i][1]))):
                    dp[k][i] = (cand_score, sorted(cand_indices))
        # Find the best among k=1..4
        best = (0, [])
        for k in range(1, 5):
            if (dp[k][n][0] > best[0] or (dp[k][n][0] == best[0] and dp[k][n][1] < best[1])):
                best = dp[k][n]
        # Verification: Ensure chosen intervals are non-overlapping
        chosen = [intervals[i] for i in best[1]]
        chosen_sorted = sorted((li, ri) for li, ri, _ in chosen)
        for i in range(1, len(chosen_sorted)):
            if chosen_sorted[i-1][1] >= chosen_sorted[i][0]:
                return [] # Invalid selection
        return sorted(best[1])
# @lc code=end