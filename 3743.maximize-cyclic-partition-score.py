#
# @lc app=leetcode id=3743 lang=python3
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Duplicate nums to simulate wrap-around
        nums = nums + nums[:k-1]
        n2 = len(nums)
        dp = [0] * n2
        max_score = 0
        for i in range(n):
            min_val = float('inf')
            max_val = float('-inf')
            for j in range(i, i + k):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                dp[j] = max(dp[j], max_val - min_val)
                max_score = max(max_score, sum(dp[i:i+k]))
        return max_score # @lc code=end