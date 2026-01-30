#
# @lc app=leetcode id=3677 lang=python3
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        def generate_palindrome(half, odd_length):
            """ Generate a full palindrome from half depending on length type """
            half_bin = bin(half)[2:]
            if odd_length:
                return int(half_bin + half_bin[-2::-1], 2)
            else:
                return int(half_bin + half_bin[::-1], 2)
        
        count = 0
        length = len(bin(n)) - 2  # Calculate the length of the binary representation of n
        for l in range(1, length + 1):
            # Even and odd length palindromes
            for half in range(1 << ((l + 1) // 2)):
                palindrome = generate_palindrome(half, l % 2 != 0)
                if palindrome > n:
                    break
                count += 1
        return count
# @lc code=end