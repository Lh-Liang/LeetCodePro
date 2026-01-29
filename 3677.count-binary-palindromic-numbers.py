#
# @lc app=leetcode id=3677 lang=python3
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1
        s = bin(n)[2:]
        L = len(s)
        smaller = 0
        for m in range(1, L):
            free = ((m + 1) // 2) - 1
            smaller += (1 << free)
        half = (L + 1) // 2
        prefix_bin = s[:half]
        prefix_int = int(prefix_bin, 2)
        min_left = 1 << (half - 1)
        lenL_count = max(0, prefix_int - min_left)
        mirror_len = L - half
        rev_bin = prefix_bin[:mirror_len][::-1]
        cand_str = prefix_bin + rev_bin
        cand = int(cand_str, 2)
        if cand <= n:
            lenL_count += 1
        return smaller + lenL_count + 1

# @lc code=end