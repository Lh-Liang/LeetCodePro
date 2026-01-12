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
        
        s_n = bin(n)[2:]
        L = len(s_n)
        
        # Count for length 1: "0" and "1"
        total_count = 2
        
        # Count for lengths i such that 1 < i < L
        for i in range(2, L):
            half_len = (i + 1) // 2
            total_count += 1 << (half_len - 1)
            
        # Count for length L (if L > 1)
        if L > 1:
            half_len = (L + 1) // 2
            prefix_s = s_n[:half_len]
            H = int(prefix_s, 2)
            P = 1 << (half_len - 1)
            
            # Number of palindromes of length L with prefix < H
            total_count += (H - P)
            
            # Check if palindrome with prefix H is <= n
            if L % 2 == 0:
                # Even length: mirror the whole prefix
                palindrome_s = prefix_s + prefix_s[::-1]
            else:
                # Odd length: mirror the prefix except the last bit
                palindrome_s = prefix_s + prefix_s[:-1][::-1]
            
            if int(palindrome_s, 2) <= n:
                total_count += 1
                
        return total_count
# @lc code=end