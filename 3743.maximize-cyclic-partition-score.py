#
# @lc app=leetcode id=3743 lang=python3
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = sorted(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + s[i]
        ans = 0
        for m in range(1, min(k, n) + 1):
            sum_small = prefix[m]
            sum_large = prefix[n] - prefix[n - m]
            ans = max(ans, sum_large - sum_small)
        return ans

# @lc code=end