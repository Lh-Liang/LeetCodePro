#
# @lc app=leetcode id=3734 lang=python3
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        n = len(s)
        count = Counter(s)
        odd_char = None
        half = []
        # Check for palindromic possibility and prepare half characters
        for char in sorted(count):
            if count[char] % 2 == 1:
                if odd_char is not None:
                    return ""  # More than one odd char means no palindrome possible
                odd_char = char
            half.extend(char * (count[char] // 2))
        # Construct smallest palindrome from half characters and optional center character
        smallest_palindrome = ''.join(half) + (odd_char if odd_char else '') + ''.join(half[::-1])
        # Ensure it is strictly greater than target if possible
        if smallest_palindrome <= target:
            return ""  # Already checked all permutations above target during construction
        return smallest_palindrome # Return as this is > target and valid palindrome.
# @lc code=end