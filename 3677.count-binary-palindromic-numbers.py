#
# @lc app=leetcode id=3677 lang=python3
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        def generate_palindromes(length):
            """Generate all binary palindromes of a given length."""
            if length == 1: # single digit palindrome is trivial
                return ['0', '1']
            half_len = (length + 1) // 2 
            palindromes = []
            for i in range(1 << (half_len - 1), 1 << half_len): # avoid leading zeroes
                half = bin(i)[2:] # convert to binary and remove '0b'
                if length % 2 == 0:
                    palindromes.append(half + half[::-1])
                else:
                    palindromes.append(half + half[-2::-1])
            return palindromes
        
        count = 0
        max_length = len(bin(n)) - 2 # Get bit length of n without '0b'
        for bit_length in range(1, max_length + 1):
            for palindrome in generate_palindromes(bit_length):
                if int(palindrome, 2) <= n:
                    count += 1
        return count
# @lc code=end