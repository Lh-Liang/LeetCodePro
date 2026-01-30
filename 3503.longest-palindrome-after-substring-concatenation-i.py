#
# @lc app=leetcode id=3503 lang=python3
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        from collections import Counter
        
        # Count frequencies of each character in s and t
        count_s = Counter(s)
        count_t = Counter(t)
        
        max_len = 0
        center_char_used = False
        
        # Check all possible characters for pairing
        for char in set(s + t):
            pairs = min(count_s.get(char, 0), count_t.get(char, 0))
            max_len += 2 * pairs  # Each pair adds two to the length of palindrome
            
            # Check if there's potential for a center character (odd count)
            if not center_char_used and (count_s.get(char, 0) > pairs or count_t.get(char, 0) > pairs):
                max_len += 1  # Add one for a center character if available
                center_char_used = True
        
        return max_len
# @lc code=end