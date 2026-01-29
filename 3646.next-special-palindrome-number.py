#
# @lc app=leetcode id=3646 lang=python3
#
# [3646] Next Special Palindrome Number
#
# @lc code=start
from itertools import combinations

class Solution:
    def specialPalindrome(self, n: int) -> int:
        s_n = str(n)
        len_n = len(s_n)
        candidates = []

        # Iterate through all possible subsets of digits 1-9
        for r in range(1, 10):
            for subset in combinations(range(1, 10), r):
                length = sum(subset)
                if length < len_n:
                    continue
                
                # Check parity constraints for palindrome
                odds = [d for d in subset if d % 2 != 0]
                if length % 2 == 0:
                    if len(odds) > 0: continue
                    mid_digit = None
                else:
                    if len(odds) != 1: continue
                    mid_digit = odds[0]
                
                # Required counts for the first half (including center if odd)
                half_counts = {d: d // 2 for d in subset}
                if mid_digit is not None:
                    half_counts[mid_digit] += 1
                
                res = self.get_min_greater(length, half_counts, mid_digit, s_n if length == len_n else None)
                if res is not None:
                    candidates.append(res)
        
        return min(candidates) if candidates else -1

    def get_min_greater(self, length, half_counts, mid_digit, limit_str):
        m = (length + 1) // 2

        def build(prefix_list):
            s = "".join(map(str, prefix_list))
            if length % 2 == 0:
                return int(s + s[::-1])
            else:
                return int(s + s[:-1][::-1])

        if limit_str is None:
            # Case: length > len(n). Build smallest possible.
            res_prefix = []
            counts = half_counts.copy()
            for i in range(m):
                for d in range(1, 10):
                    if counts.get(d, 0) > 0:
                        res_prefix.append(d)
                        counts[d] -= 1
                        break
            return build(res_prefix)

        # Case: length == len(n). 
        n_val = int(limit_str)
        best = float('inf')
        
        # 1. Try matching prefix exactly
        counts = half_counts.copy()
        match_prefix = []
        possible = True
        for i in range(m):
            d = int(limit_str[i])
            if counts.get(d, 0) > 0:
                match_prefix.append(d)
                counts[d] -= 1
            else:
                possible = False
                break
        if possible:
            p = build(match_prefix)
            if p > n_val: best = min(best, p)

        # 2. Try changing at index i to something larger, then minimize rest
        for i in range(m - 1, -1, -1):
            counts = half_counts.copy()
            prefix_fixed = []
            can_match = True
            for j in range(i):
                d = int(limit_str[j])
                if counts.get(d, 0) > 0:
                    prefix_fixed.append(d)
                    counts[d] -= 1
                else:
                    can_match = False
                    break
            if not can_match: continue
            
            # Try d > limit_str[i]
            for d in range(int(limit_str[i]) + 1, 10):
                if counts.get(d, 0) > 0:
                    temp_counts = counts.copy()
                    temp_prefix = prefix_fixed + [d]
                    temp_counts[d] -= 1
                    # Fill remaining with smallest possible
                    for _ in range(i + 1, m):
                        for d_low in range(1, 10):
                            if temp_counts.get(d_low, 0) > 0:
                                temp_prefix.append(d_low)
                                temp_counts[d_low] -= 1
                                break
                    best = min(best, build(temp_prefix))
                    break # Found smallest for this index i
        
        return best if best != float('inf') else None
# @lc code=end