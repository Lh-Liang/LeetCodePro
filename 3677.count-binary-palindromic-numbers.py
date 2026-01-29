#
# @lc app=leetcode id=3677 lang=python3
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        def generate_palindrome(length, is_odd):
            # Generates a palindromic binary number of given length
            half_length = (length + is_odd) // 2
            start = 1 << (half_length - 1)
            end = 1 << half_length
            for i in range(start, end):
                left_half = bin(i)[2:]
                if is_odd:
                    yield int(left_half + left_half[-2::-1], 2)
                else:
                    yield int(left_half + left_half[::-1], 2)
        count = 0
        # Early termination loop for generated palindromes exceeding `n`
        length = len(bin(n)) - 2 # Length of the largest possible binary palindrome
        for l in range(1, length + 1):
            for is_odd in [0, 1]:
                for p in generate_palindrome(l, is_odd):
                    if p > n:
                        return count
                    count += 1
        return count
# @lc code=end