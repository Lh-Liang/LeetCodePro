#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Step 1: Sort intervals based on their ending points.
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        
        # Step 2 & 3: Use dynamic programming to find max weight of up to 4 non-overlapping intervals.
        dp = [[0] * (5) for _ in range(n + 1)] # dp[i][j] - max score using first i intervals choosing j intervals.
        best_intervals = [[[] for _ in range(5)] for _ in range(n + 1)] # To store indices of chosen intervals.

        for i in range(1, n + 1):
            l_i, r_i, w_i = intervals[i-1]
            dp[i] = dp[i-1][:] # Start with previous values.
            best_intervals[i] = [list(b) for b in best_intervals[i-1]] # Copy previous interval choices.
            
            # Consider current interval as one of our choices:
            for j in range(1, 5): # Because we can choose up to 4 intervals.
                k = i - 1 # Find last interval that does not overlap with current one using binary search or linear scan.
                while k >= 0 and intervals[k][1] >= l_i:
                    k -= 1
                if dp[k+1][j-1] + w_i > dp[i][j]:
                    dp[i][j] = dp[k+1][j-1] + w_i
                    best_intervals[i][j] = best_intervals[k+1][j-1] + [i-1]
                elif dp[k+1][j-1] + w_i == dp[i][j]: # If same score, take lexicographically smallest set.
                    candidate_set = best_intervals[k+1][j-1] + [i-1]
                    if candidate_set < best_intervals[i][j]:
                        best_intervals[i][j] = candidate_set[:] 
        
        # Step 6: We need maximum of any choice from using up to 4 non-overlapping intervals. 
        max_score = max(dp[n]) 
        max_j = dp[n].index(max_score) 
        return sorted(best_intervals[n][max_j])
# @lc code=end