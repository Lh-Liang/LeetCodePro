#
# @lc app=leetcode id=3677 lang=python3
#
# [3677] Count Binary Palindromic Numbers
#
# @lc code=start
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        def create_palindrome(first_half, is_odd):
            res = first_half
            if is_odd:
                first_half //= 2
            while first_half > 0:
                res = (res << 1) | (first_half & 1)
                first_half //= 2
            return res

        count = 0
        max_len = n.bit_length()
        # For odd and even length palindromes
        for length in range(1, max_len + 1):
            half_len = (length + 1) // 2
            # The first bit must be 1 (except for length 1), so range starts at 1 for length > 1
            start = 1 << (half_len - 1) if length > 1 else 0
            end = 1 << half_len
            for first_half in range(start, end):
                p = create_palindrome(first_half, length % 2)
                if p > n:
                    break
                count += 1
        return count
# @lc code=end