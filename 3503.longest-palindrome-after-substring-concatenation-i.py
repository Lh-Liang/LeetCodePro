#
# @lc app=leetcode id=3503 lang=python3
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def expand_around_center(string, left, right):
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        # Try all possible ways to split s and t
        max_len = 0
        
        # Case 1: Take substring only from s
        for i in range(len(s)):
            # Odd length palindrome
            length = expand_around_center(s, i, i)
            max_len = max(max_len, length)
            # Even length palindrome
            length = expand_around_center(s, i, i + 1)
            max_len = max(max_len, length)
        
        # Case 2: Take substring only from t
        for i in range(len(t)):
            # Odd length palindrome
            length = expand_around_center(t, i, i)
            max_len = max(max_len, length)
            # Even length palindrome
            length = expand_around_center(t, i, i + 1)
            max_len = max(max_len, length)
        
        # Case 3: Take prefix from s and suffix from t
        # For each character in s and each character in t
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    # Try to expand around this matching pair
                    left, right = i, j
                    length = 0
                    while left >= 0 and right < len(t) and s[left] == t[right]:
                        left -= 1
                        right += 1
                        length += 2
                    max_len = max(max_len, length)
        
        # Case 4: Take suffix from s and prefix from t
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    # Try to expand around this matching pair
                    left, right = i, j
                    length = 0
                    while left < len(s) and right >= 0 and s[left] == t[right]:
                        left += 1
                        right -= 1
                        length += 2
                    max_len = max(max_len, length)
        
        return max_len
# @lc code=end