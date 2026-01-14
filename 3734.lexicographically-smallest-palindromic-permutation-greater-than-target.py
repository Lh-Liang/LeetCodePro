#
# @lc app=leetcode id=3734 lang=python3
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#
# @lc code=start
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        
        freq = Counter(s)
        
        # Check if palindrome is possible
        odd_count = sum(1 for c in freq.values() if c % 2 == 1)
        if odd_count > 1:
            return ""
        
        # Build half and middle
        half = []
        middle = ""
        for char in sorted(freq.keys()):
            count = freq[char]
            half.extend([char] * (count // 2))
            if count % 2 == 1:
                middle = char
        
        half.sort()
        
        def make_palindrome(h, mid):
            return ''.join(h) + mid + ''.join(reversed(h))
        
        def next_permutation(arr):
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            
            if i == -1:
                return False
            
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = arr[i + 1:][::-1]
            
            return True
        
        current_half = half[:]
        while True:
            palindrome = make_palindrome(current_half, middle)
            if palindrome > target:
                return palindrome
            if not next_permutation(current_half):
                break
        
        return ""
# @lc code=end