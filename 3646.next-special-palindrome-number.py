#
# @lc app=leetcode id=3646 lang=python3
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
import itertools
from bisect import bisect_right

class Solution:
    def specialPalindrome(self, n: int) -> int:
        special_numbers = []
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        # Find all subsets of {1..9} with at most one odd number
        for r in range(1, 10):
            for subset in itertools.combinations(digits, r):
                odds = [d for d in subset if d % 2 != 0]
                if len(odds) > 1:
                    continue
                
                total_len = sum(subset)
                if total_len > 17: # Constraints go up to 10^15, but allow some margin
                    continue
                
                mid = str(odds[0]) if odds else ""
                half_elements = []
                for d in subset:
                    count = (d - 1) // 2 if d % 2 != 0 else d // 2
                    half_elements.extend([str(d)] * count)
                
                # Generate all unique permutations of the half part
                seen_perms = set()
                for p in itertools.permutations(half_elements):
                    if p in seen_perms:
                        continue
                    seen_perms.add(p)
                    
                    # No leading zeros (though digits are 1-9, good practice)
                    if p and p[0] == '0':
                        continue
                    
                    half_str = "".join(p)
                    full_str = half_str + mid + half_str[::-1]
                    special_numbers.append(int(full_str))
        
        special_numbers.sort()
        idx = bisect_right(special_numbers, n)
        
        return special_numbers[idx] if idx < len(special_numbers) else -1
# @lc code=end