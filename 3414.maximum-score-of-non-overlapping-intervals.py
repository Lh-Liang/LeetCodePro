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
        # (l, r, w, idx)
        ints = [(inter[0], inter[1], inter[2], i) for i, inter in enumerate(intervals)]
        ints.sort(key=lambda x: x[1])
        ends = [x[1] for x in ints]
        dp = [[(-1 if j > 0 else 0, []) for j in range(5)] for _ in range(n + 1)]
        dp[0][0] = (0, [])
        for i in range(1, n + 1):
            curr_l, curr_r, curr_w, curr_idx = ints[i - 1]
            # binary search largest pos < i-1 s.t. ends[pos] < curr_l (strict)
            pos = bisect.bisect_left(ends, curr_l, 0, i - 1) - 1
            prev_max_i = pos + 1 if pos >= 0 else 0
            dp[i][0] = (0, [])
            for j in range(1, 5):
                score_not, path_not = dp[i - 1][j]
                best_score = score_not
                best_path = path_not[:]
                # take
                prev_score = dp[prev_max_i][j - 1][0]
                if prev_score >= 0:
                    prev_path = dp[prev_max_i][j - 1][1]
                    take_score = prev_score + curr_w
                    take_path = sorted(prev_path + [curr_idx])
                    if (take_score > best_score or
                        (take_score == best_score and take_path < best_path)):
                        best_score = take_score
                        best_path = take_path
                dp[i][j] = (best_score, best_path)
        # find best
        max_score = 0
        best_path = []
        for j in range(5):
            score, path = dp[n][j]
            if score > max_score or (score == max_score and (not best_path or path < best_path)):
                max_score = score
                best_path = path
        return best_path
# @lc code=end