#
# @lc app=leetcode id=3538 lang=python3
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        # Initialize DP table with infinity values
        dp = [[float('inf')] * n for _ in range(k + 1)]
        
        # Base case initialization for 0 merges
        for i in range(n - 1):
            dp[0][i] = (position[i + 1] - position[i]) * time[i]
        
        # Fill DP table for each number of merges from 1 to k
        for merges in range(1, k + 1):
            # Iterate over segments considering merge possibilities
            for i in range(n - merges):
                # Attempt to merge current segment with subsequent ones
                min_cost = float('inf')
                current_time = time[i]
                for j in range(i, n - merges):
                    if j > i:
                        current_time += time[j]
                    segment_length = position[j + 1] - position[i]
                    min_cost = min(min_cost, dp[merges - 1][j] + segment_length * current_time)
                dp[merges][i] = min_cost
        
        # Calculate minimum total travel time after exactly k merges
        return min(dp[k][i] for i in range(n - k))
# @lc code=end