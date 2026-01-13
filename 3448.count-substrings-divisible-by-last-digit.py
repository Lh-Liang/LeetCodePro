#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[d] is a list of length d: counts of substrings ending at current position with remainder r mod d
        dp = {d: [0] * d for d in range(1, 10)}
        ans = 0

        for ch in s:
            x = ord(ch) - 48
            for d in range(1, 10):
                prev = dp[d]
                new = [0] * d

                # extend all previous substrings by digit x
                for r, cnt in enumerate(prev):
                    if cnt:
                        new[(r * 10 + x) % d] += cnt

                # start a new substring at this position
                new[x % d] += 1

                dp[d] = new

            if x != 0:
                ans += dp[x][0]

        return ans
# @lc code=end
