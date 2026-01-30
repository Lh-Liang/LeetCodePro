#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Sort intervals based on their end time (ri)
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        # Initialize dp with tuples of (max_score, indices_list)
        dp = [(0, [])] * (n + 1)
        for i in range(1, n+1):
            li, ri, wi = intervals[i-1]
            # Binary search for last interval that doesn't overlap with current one
            low, high = 0, i-1
            while low < high:
                mid = (low + high + 1) // 2
                if intervals[mid][1] < li:
                    low = mid + 1
                else:
                    high = mid - 1
            prev_index = low - 1 if intervals[low][1] < li else -1
            # Calculate new score if including this interval
            new_score = dp[prev_index+1][0] + wi if prev_index != -1 else wi
            new_indices = dp[prev_index+1][1] + [i-1] if prev_index != -1 else [i-1]
            # Update dp table with max score and lexicographically smallest indices list
            if new_score > dp[i-1][0]:
                dp[i] = (new_score, sorted(new_indices)[:4])  # at most 4 indices allowed
            elif new_score == dp[i-1][0]: 
                dp[i] = min(dp[i], (new_score, sorted(new_indices)[:4]))
            else:
                dp[i] = dp[i-1]
        return sorted(dp[-1][1])
# @lc code=end