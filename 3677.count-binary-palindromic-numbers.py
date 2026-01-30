#
# @lc app=leetcode id=3677 lang=python3
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        res = 0
        L = n.bit_length()
        seen = set()  # To ensure uniqueness
        # Generate palindromic numbers for each possible length
        for l in range(1, L+1):
            half = (l + 1) // 2
            for i in range(1 << (half - 1), 1 << half):
                s = bin(i)[2:]
                if l % 2 == 0:
                    p = s + s[::-1]
                else:
                    p = s + s[::-1][1:]
                val = int(p, 2)
                if val <= n and val not in seen:
                    seen.add(val)
                    res += 1
        # Ensure 0 is counted exactly once if in range
        if 0 <= n:
            res += 1 if 0 not in seen else 0
        # Verification: All palindromic numbers are unique and <= n
        assert all(x <= n for x in seen)
        return res
# @lc code=end