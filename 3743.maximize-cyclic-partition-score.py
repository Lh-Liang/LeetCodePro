#
# @lc app=leetcode id=3743 lang=python3
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Double nums for easier cyclic handling
        extended_nums = nums + nums
        
        # Initialize DP table for storing maximum scores
        dp = [[0] * (k + 1) for _ in range(2 * n)]
        
        # Base case for one partition
        for i in range(n):
            current_min = float('inf')
            current_max = float('-inf')
            # Calculate range directly for single partitions up to n elements forward
            for j in range(i, i + n):
                idx = j % n
                current_min = min(current_min, extended_nums[idx])
                current_max = max(current_max, extended_nums[idx])
                current_range = current_max - current_min
                dp[i][1] = max(dp[i][1], current_range)
        
        # Fill DP table for more than one partition allowed
        for p in range(2, k + 1):
            for i in range(n):
                current_min = float('inf')
                current_max = float('-inf')
                # Iterate and calculate possible partition scores
                for j in range(i, i + n):
                    idx = j % n
                    current_min = min(current_min, extended_nums[idx])
                    current_max = max(current_max, extended_nums[idx])
                    current_range = current_max - current_min
                    prev_idx = (j + 1) % n if j + 1 < i + n else i % n
                    dp[i][p] = max(dp[i][p], dp[prev_idx][p - 1] + current_range)
        
        # Return the maximum score found across all starting points with k partitions allowed
        return max(dp[i][k] for i in range(n))
# @lc code=end