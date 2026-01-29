#
# @lc app=leetcode id=3734 lang=python3
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Check if a palindromic permutation is possible
        odd_chars = [c for c, count in counts.items() if count % 2 == 1]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = {c: count // 2 for c, count in counts.items() if count // 2 > 0}
        
        L = n // 2
        target_half = target[:L]
        
        # Case 1: Try using the target's first half exactly
        current_half_counts = Counter(half_counts)
        can_match_prefix = True
        for char in target_half:
            if current_half_counts[char] > 0:
                current_half_counts[char] -= 1
            else:
                can_match_prefix = False
                break
        
        if can_match_prefix:
            candidate = target_half + mid_char + target_half[::-1]
            if candidate > target:
                return candidate
        
        # Case 2: Find the rightmost position to increment a character in the first half
        # Track the character counts for the prefix as we backtrack
        prefix_counts = Counter(half_counts)
        for i in range(L):
            if i < len(target_half):
                prefix_counts[target_half[i]] -= 1
                
        for i in range(L - 1, -1, -1):
            # Add target_half[i] back to available characters for the suffix
            char_at_i = target_half[i]
            prefix_counts[char_at_i] += 1
            
            # Try to find a character > target_half[i] to place at index i
            for char_code in range(ord(char_at_i) + 1, ord('z') + 1):
                c = chr(char_code)
                if prefix_counts[c] > 0:
                    # Found the rightmost point of divergence
                    res_half = list(target_half[:i])
                    res_half.append(c)
                    prefix_counts[c] -= 1
                    
                    # Fill the rest of the half with the smallest available characters
                    for small_char_code in range(ord('a'), ord('z') + 1):
                        sc = chr(small_char_code)
                        if prefix_counts[sc] > 0:
                            res_half.extend([sc] * prefix_counts[sc])
                    
                    h = "".join(res_half)
                    return h + mid_char + h[::-1]
                    
        return ""
# @lc code=end