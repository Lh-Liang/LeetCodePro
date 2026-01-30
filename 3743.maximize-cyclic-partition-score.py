#
# @lc app=leetcode id=3743 lang=python3
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums2 = nums + nums
        # Precompute range for all windows
        range_table = [[0]*n for _ in range(n)]
        for i in range(n):
            mx = mn = nums[i]
            for j in range(i, i+n):
                mx = max(mx, nums2[j])
                mn = min(mn, nums2[j])
                if j-i < n:
                    range_table[i][j-i] = mx - mn
        # Optional: Verify range_table for sample intervals
        # assert range_table[0][n-1] == max(nums) - min(nums)
        res = 0
        for start in range(n):
            dp = [[-float('inf')] * (k+1) for _ in range(n+1)]
            dp[0][0] = 0
            for i in range(1, n+1):
                for p in range(1, min(k, i)+1):
                    for j in range(p-1, i):
                        prev = dp[j][p-1]
                        rng = range_table[(start+j)%n][i-j-1]
                        if prev + rng > dp[i][p]:
                            dp[i][p] = prev + rng
            # Optional: Check DP states after computation
            # for p in range(1, k+1):
            #     assert dp[n][p] >= 0
            res = max(res, max(dp[n][1:k+1]))
        return res
# @lc code=end