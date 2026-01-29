#
# @lc app=leetcode id=3743 lang=python3
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Dynamic programming table to store max scores for different partitions
        dp = [[-float('inf')] * (k + 1) for _ in range(n)]
        
        # Precompute max-min ranges in a cyclic manner for all possible starts and lengths
        for start in range(n):
            current_max = nums[start]
            current_min = nums[start]
            # Calculate ranges for subarray lengths from start position
            for length in range(n):
                idx = (start + length) % n
                current_max = max(current_max, nums[idx])
                current_min = min(current_min, nums[idx])
                range_score = current_max - current_min
                if length == n - 1:
                    # Single partition covering whole array case
                    dp[start][1] = range_score
                else:
                    # Update dp table for possible additional partitions
                    for p in range(2, k + 1):
                        next_start_idx = (idx + 1) % n
                        if length + 1 < n:
                            dp[start][p] = max(dp[start][p], range_score + dp[next_start_idx][p - 1])
        
        # Return the best score obtainable starting from any index with k full partitions available.
        return max(dp[i][k] for i in range(n))
# @lc code=end