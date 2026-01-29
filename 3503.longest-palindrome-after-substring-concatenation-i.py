#
# @lc app=leetcode id=3503 lang=python3
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        max_len = 0
        
        # Pre-calculate substrings to avoid repeated slicing in nested loops
        s_subs = [s[i:j] for i in range(n + 1) for j in range(i, n + 1)]
        t_subs = [t[i:j] for i in range(m + 1) for j in range(i, m + 1)]
        
        for sub_s in s_subs:
            for sub_t in t_subs:
                combined_len = len(sub_s) + len(sub_t)
                if combined_len > max_len:
                    combined = sub_s + sub_t
                    if combined == combined[::-1]:
                        max_len = combined_len
        
        return max_len
# @lc code=end