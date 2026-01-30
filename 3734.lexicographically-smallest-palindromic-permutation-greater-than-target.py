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
        counter = Counter(s)
        odd_chars = [ch for ch, cnt in counter.items() if cnt % 2 == 1]
        if len(odd_chars) > 1:
            return ''
        # Build smallest palindromic permutation
        half = []
        mid = odd_chars[0] if odd_chars else ''
        for ch in sorted(counter):
            half.extend([ch] * (counter[ch] // 2))
        half_str = ''.join(half)
        def build_palindrome(h):
            return h + mid + h[::-1]
        def is_valid_permutation(pal):
            from collections import Counter
            return Counter(pal) == counter
        cand = build_palindrome(half_str)
        if cand > target and is_valid_permutation(cand):
            return cand
        # Next lexicographical palindromic permutation
        half_list = list(half_str)
        def next_permutation(arr):
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i+1]:
                i -= 1
            if i == -1:
                return False
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i+1:] = reversed(arr[i+1:])
            return True
        while next_permutation(half_list):
            cand = build_palindrome(''.join(half_list))
            if cand > target and is_valid_permutation(cand):
                return cand
        return ''
# @lc code=end