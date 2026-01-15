#
# @lc app=leetcode id=3743 lang=python3
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        doubled = nums + nums
        effective_k = min(k, n)
        ans = 0
        
        for s in range(n):
            arr = doubled[s:s+n]
            
            # Precompute ranges for all subarrays
            ranges = [[0] * (n + 1) for _ in range(n)]
            for i in range(n):
                mx = mn = arr[i]
                for j in range(i, n):
                    mx = max(mx, arr[j])
                    mn = min(mn, arr[j])
                    ranges[i][j + 1] = mx - mn
            
            # DP: dp[i] = max score for first i elements
            dp = [float('-inf')] * (n + 1)
            dp[0] = 0
            
            for _ in range(effective_k):
                ndp = [float('-inf')] * (n + 1)
                for i in range(1, n + 1):
                    for p in range(i):
                        if dp[p] > float('-inf'):
                            ndp[i] = max(ndp[i], dp[p] + ranges[p][i])
                dp = ndp
                if dp[n] > float('-inf'):
                    ans = max(ans, dp[n])
        
        return ans
# @lc code=end