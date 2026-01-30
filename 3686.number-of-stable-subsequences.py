#
# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # dp1: end with one element of parity p, dp2: end with two consecutive elements of parity p
        dp1 = [0, 0]  # [even, odd]
        dp2 = [0, 0]  # [even, odd]
        total = 0
        for num in nums:
            p = num % 2
            q = 1 - p
            # New subsequence with current num
            new_dp1 = dp1.copy()
            new_dp2 = dp2.copy()
            # Start a new subsequence with current num
            cnt_dp1 = 1
            # Extend all subsequences ending with parity q (other parity):
            cnt_dp1 = (cnt_dp1 + dp1[q] + dp2[q]) % MOD
            # Extend subsequences ending with one current parity
            cnt_dp2 = dp1[p] % MOD
            # Update for this round
            new_dp1[p] = cnt_dp1
            new_dp2[p] = cnt_dp2
            dp1 = new_dp1
            dp2 = new_dp2
        total = (dp1[0] + dp1[1] + dp2[0] + dp2[1]) % MOD
        return total
# @lc code=end