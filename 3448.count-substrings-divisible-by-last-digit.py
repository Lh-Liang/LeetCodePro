#
# @lc app=leetcode id=3448 lang=python3
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        freq = [[0] * 10 for _ in range(10)]
        ans = 0
        for i in range(n):
            dig = ord(s[i]) - ord('0')
            if dig > 0:
                dd = dig
                count = 1
                for m in range(dd):
                    if (m * 10 + dig) % dd == 0:
                        count += freq[dd][m]
                ans += count
            for dd in range(1, 10):
                new_freq = [0] * 10
                for m in range(dd):
                    nm = (m * 10 + dig) % dd
                    new_freq[nm] += freq[dd][m]
                ns = dig % dd
                new_freq[ns] += 1
                freq[dd] = new_freq[:]
        return ans
# @lc code=end