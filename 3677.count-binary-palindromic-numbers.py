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
        
        def construct_palindrome(first_half, L):
            s = bin(first_half)[2:]
            if L % 2 == 0:
                return int(s + s[::-1], 2)
            else:
                return int(s + s[-2::-1], 2)
        
        count = 1  # Count "0"
        L = n.bit_length()
        
        # Count palindromes of length 1 to L-1
        for l in range(1, L):
            if l == 1:
                count += 1
            else:
                m = (l + 1) // 2
                count += 1 << (m - 1)
        
        # Count palindromes of length L that are <= n using binary search
        m = (L + 1) // 2
        lo, hi = 1 << (m - 1), (1 << m) - 1
        result = lo - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            palindrome = construct_palindrome(mid, L)
            if palindrome <= n:
                result = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        if result >= 1 << (m - 1):
            count += result - (1 << (m - 1)) + 1
        
        return count
# @lc code=end