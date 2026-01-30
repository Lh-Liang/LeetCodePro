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
        # dp[length][parity1][parity2]:
        # number of subsequences of given length ending with parities parity1, parity2
        # Only track subsequences of up to length 2 for stability checking
        # dp0: count of empty subsequence (for initialization)
        dp = {}  # (len, last1, last2) -> count
        ans = 0
        for num in nums:
            p = num % 2
            new_dp = {}
            # Start a new subsequence with this number
            new_dp[(1, p, -1)] = (new_dp.get((1, p, -1), 0) + 1) % MOD
            # Extend existing subsequences
            for (length, last1, last2), count in dp.items():
                # Exclude current num: keep old state
                new_dp[(length, last1, last2)] = (new_dp.get((length, last1, last2), 0) + count) % MOD
                # Try to include current num
                if length == 1:
                    # Add as second element
                    new_dp[(2, last1, p)] = (new_dp.get((2, last1, p), 0) + count) % MOD
                elif length == 2:
                    # Add as third element, check stability
                    if not (last1 == last2 == p):
                        new_dp[(2, last2, p)] = (new_dp.get((2, last2, p), 0) + count) % MOD
            dp = new_dp
        # Sum all non-empty subsequences
        for (length, last1, last2), count in dp.items():
            ans = (ans + count) % MOD
        return ans
# @lc code=end