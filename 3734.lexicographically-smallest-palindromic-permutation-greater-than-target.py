#
# @lc app=leetcode id=3734 lang=python3
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        from itertools import permutations
        
        char_counts = Counter(s)
        odd_char = None
        half_palindrome = []
        for char in sorted(char_counts):
            count = char_counts[char]
            if count % 2 == 1:
                if odd_char is not None:
                    return "" # More than one character with an odd count
                odd_char = char
            half_palindrome.append(char * (count // 2))
        
        # Create a list from half_palindrome string for permutations
        half_chars = ''.join(half_palindrome)
        
        # Generate all unique permutations of half_chars and form palindromes
        unique_half_permutations = set(permutations(half_chars))
        sorted_palindromes = []
        for perm in unique_half_permutations:
            half_perm_str = ''.join(perm)
            full_palindrome = half_perm_str + (odd_char or '') + half_perm_str[::-1]
            sorted_palindromes.append(full_palindrome)
        
        # Sort palindromes lexicographically
        sorted_palindromes.sort()
        
        # Find the first palindrome greater than target
        for palindrome in sorted_palindromes:
            if palindrome > target:
                return palindrome
                
        return "" # Return empty string if no valid greater palindrome can be formed.
# @lc code=end