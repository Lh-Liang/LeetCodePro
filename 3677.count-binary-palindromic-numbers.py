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
        B = len(s)
        
        # Start with 1 to account for 0 ("0")
        ans = 1
        
        # 1. Count binary palindromes with bit length L < B
        for L in range(1, B):
            if L == 1:
                ans += 1 # Only "1"
            else:
                # First bit fixed as 1, ceil(L/2) - 1 free bits
                half = (L + 1) // 2
                ans += (1 << (half - 1))
        
        # 2. Count binary palindromes with bit length B
        K = (B + 1) // 2
        prefix_str = s[:K]
        P = int(prefix_str, 2)
        
        # Construct the palindrome from the prefix P
        if B % 2 == 0:
            cand_str = prefix_str + prefix_str[::-1]
        else:
            cand_str = prefix_str + prefix_str[:-1][::-1]
            
        cand = int(cand_str, 2)
        
        # Smallest K-bit prefix starting with 1
        min_prefix = 1 << (K - 1)
        
        if cand <= n:
            # All prefixes in [min_prefix, P] are valid
            ans += (P - min_prefix + 1)
        else:
            # All prefixes in [min_prefix, P - 1] are valid
            if P > min_prefix:
                ans += (P - min_prefix)
                
        return ans
# @lc code=end