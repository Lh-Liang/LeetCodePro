#
# @lc app=leetcode id=3646 lang=python3
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
from itertools import combinations
import bisect

class Solution:
    def specialPalindrome(self, n: int) -> int:
        def next_permutation(arr):
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i < 0:
                return False
            j = len(arr) - 1
            while arr[i] >= arr[j]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i+1:] = arr[i+1:][::-1]
            return True
        
        def all_unique_perms(elements):
            if not elements:
                return [()]
            arr = sorted(elements)
            result = [tuple(arr)]
            while next_permutation(arr):
                result.append(tuple(arr))
            return result
        
        even_digits = [2, 4, 6, 8]
        odd_digits = [1, 3, 5, 7, 9]
        
        all_palindromes = []
        max_length = 25
        
        # Generate even length palindromes
        for r in range(1, 5):
            for combo in combinations(even_digits, r):
                length = sum(combo)
                if length <= max_length:
                    half = []
                    for d in combo:
                        half.extend([d] * (d // 2))
                    for perm in all_unique_perms(half):
                        perm_str = ''.join(map(str, perm))
                        palindrome = int(perm_str + perm_str[::-1])
                        all_palindromes.append(palindrome)
        
        # Generate odd length palindromes
        for odd_d in odd_digits:
            for r in range(0, 5):
                for even_combo in combinations(even_digits, r):
                    length = odd_d + sum(even_combo)
                    if length <= max_length:
                        half = []
                        for d in even_combo:
                            half.extend([d] * (d // 2))
                        half.extend([odd_d] * ((odd_d - 1) // 2))
                        
                        if not half:
                            all_palindromes.append(odd_d)
                        else:
                            for perm in all_unique_perms(half):
                                perm_str = ''.join(map(str, perm))
                                palindrome = int(perm_str + str(odd_d) + perm_str[::-1])
                                all_palindromes.append(palindrome)
        
        all_palindromes.sort()
        
        idx = bisect.bisect_right(all_palindromes, n)
        if idx < len(all_palindromes):
            return all_palindromes[idx]
        return -1
# @lc code=end