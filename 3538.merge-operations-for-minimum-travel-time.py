#
# @lc app=leetcode id=3538 lang=python3
#
# [3538] Merge Operations for Minimum Travel Time
#
from typing import List

# @lc code=start
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        # Initialize DP table for storing minimum travel times.
        prev_dp = [float('inf')] * n
        curr_dp = [float('inf')] * n
        
        # Base case initialization for 0 merges.
        prev_dp[0] = 0  # Start point has no distance cost.
        for j in range(1, n):
            prev_dp[j] = prev_dp[j - 1] + (position[j] - position[j - 1]) * time[j - 1]
        
        # Fill DP table for each number of merges i and endpoint j.
        for i in range(1, k + 1):
            curr_dp[0] = prev_dp[0]
            curr_dp[1] = float('inf')
            for j in range(2, n):  # Merges start only after first segment
                curr_dp[j] = prev_dp[j]
                for p in range(j):
                    # Calculate potential new minimum travel time if merging segments ending at p and p+1.
                    current_time = prev_dp[p]
                    merged_time = (position[j] - position[p]) * (time[p])
                    curr_dp[j] = min(curr_dp[j], current_time + merged_time)
            prev_dp, curr_dp = curr_dp, [float('inf')] * n
        
        # Return the minimum total travel time with exactly k merges.
        return prev_dp[n-1]
# @lc code=end