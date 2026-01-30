#
# @lc app=leetcode id=3677 lang=python3
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        count = 0
        for i in range(n + 1):
            bin_rep = bin(i)[2:]
            if bin_rep == bin_rep[::-1]:
                count += 1
        return count
# @lc code=end