#
# @lc app=leetcode id=3734 lang=python3
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
from collections import Counter
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        def next_permutation(seq):
            seq = list(seq)
            i = len(seq) - 2
            while i >= 0 and seq[i] >= seq[i + 1]:
                i -= 1
            if i == -1:
                return None
            j = len(seq) - 1
            while seq[j] <= seq[i]:
                j -= 1
            seq[i], seq[j] = seq[j], seq[i]
            seq[i + 1:] = reversed(seq[i + 1:])
            return ''.join(seq)
        
        count = Counter(s)
        mid_char = ""
        half_str = []
        for char in sorted(count):
            if count[char] % 2 == 1:
                if mid_char:
                    return ""
                mid_char = char
            half_str.extend([char] * (count[char] // 2))
        half_str = ''.join(half_str)
        palindrome_candidate = half_str + mid_char + half_str[::-1]
        if palindrome_candidate > target:
            return palindrome_candidate
        while True:
            next_half_str = next_permutation(half_str)
            if not next_half_str:
                break
            candidate = next_half_str + mid_char + next_half_str[::-1]
            if candidate > target:
                return candidate
        return ""
# @lc code=end