#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Attach original indices for reconstruction
        intervals = [(l, r, w, idx) for idx, (l, r, w) in enumerate(intervals)]
        # Sort by end time, then by index for tie-breaking
        intervals.sort(key=lambda x: (x[1], x[3]))
        n = len(intervals)
        # Precompute: for each interval, find the last interval that ends before its start
        ends = [intervals[i][1] for i in range(n)]
        starts = [intervals[i][0] for i in range(n)]
        prev = [-1] * n
        import bisect
        for i in range(n):
            # Find last j where intervals[j].end < intervals[i].start
            j = bisect.bisect_left(ends, starts[i]) - 1
            prev[i] = j
        # DP: dp[i][k] = (max_weight, path) considering first i intervals, using k intervals
        # We need only last and current, so can optimize space
        dp = [[(0, []) for _ in range(5)] for _ in range(n+1)]
        for i in range(1, n+1):
            l, r, w, idx = intervals[i-1]
            for k in range(5):
                # Option 1: skip this interval
                if dp[i-1][k][0] > dp[i][k][0] or (dp[i-1][k][0] == dp[i][k][0] and dp[i-1][k][1] < dp[i][k][1]):
                    dp[i][k] = dp[i-1][k]
                # Option 2: take this interval, if k > 0
                if k > 0:
                    pre_idx = prev[i-1] + 1
                    cand = dp[pre_idx][k-1][0] + w
                    cand_path = dp[pre_idx][k-1][1] + [idx]
                    if cand > dp[i][k][0] or (cand == dp[i][k][0] and cand_path < dp[i][k][1]):
                        dp[i][k] = (cand, cand_path)
        # Find the best among using up to 4 intervals
        best = max([dp[n][k] for k in range(1, 5)], key=lambda x: (x[0], [-1 if not x[1] else x[1]]))
        # For lex smallest, iterate from k=4 down to 1
        res = []
        max_score = -1
        for k in range(4, 0, -1):
            if dp[n][k][0] > max_score:
                max_score = dp[n][k][0]
                res = dp[n][k][1]
            elif dp[n][k][0] == max_score and dp[n][k][1] < res:
                res = dp[n][k][1]
        return sorted(res)
# @lc code=end