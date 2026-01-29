#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for d in range(1, 10):
            dp = [0] * d
            for k in range(n):
                dig = int(s[k])
                new_dp = [0] * d
                for r in range(d):
                    new_r = (r * 10 + dig) % d
                    new_dp[new_r] += dp[r]
                new_dp[dig % d] += 1
                dp = new_dp
                if dig == d:
                    ans += dp[0]
        return ans
# @lc code=end