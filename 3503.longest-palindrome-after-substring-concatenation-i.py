#
# @lc app=leetcode id=3503 lang=python3
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        # Generate all substrings of s including an empty string
        subs_s = [("", 0)]
        for i in range(n):
            for j in range(i + 1, n + 1):
                subs_s.append((s[i:j], j - i))
        
        # Generate all substrings of t including an empty string
        subs_t = [("", 0)]
        for i in range(m):
            for j in range(i + 1, m + 1):
                subs_t.append((t[i:j], j - i))
        
        max_len = 0
        # Iterate through every pair of substrings from s and t
        for sub1, l1 in subs_s:
            for sub2, l2 in subs_t:
                current_len = l1 + l2
                # Only check for palindrome if the length is better than our current best
                if current_len > max_len:
                    combined = sub1 + sub2
                    # Check if the combined string is a palindrome
                    if combined == combined[::-1]:
                        max_len = current_len
                        
        return max_len
# @lc code=end