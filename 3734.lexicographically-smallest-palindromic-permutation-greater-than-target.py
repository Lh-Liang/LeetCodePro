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
        half_len = n // 2
        
        count = Counter(s)
        
        # Check if palindrome is possible
        odd_chars = [c for c in count if count[c] % 2 == 1]
        if n % 2 == 0:
            if len(odd_chars) > 0:
                return ""
            middle = ""
        else:
            if len(odd_chars) != 1:
                return ""
            middle = odd_chars[0]
        
        # Compute available characters for the first half
        available = Counter()
        for c in count:
            available[c] = count[c] // 2
        
        def pos_to_half(i):
            if i < half_len:
                return i
            elif n % 2 == 1 and i == half_len:
                return -1  # middle position
            else:
                return n - 1 - i
        
        def try_decide_at(decision_pos):
            avail = available.copy()
            constraints = {}
            
            # Positions 0 to decision_pos-1 should equal target
            for j in range(decision_pos):
                k = pos_to_half(j)
                if k == -1:  # middle
                    if middle != target[j]:
                        return None
                else:
                    if k in constraints:
                        if constraints[k] != target[j]:
                            return None
                    else:
                        constraints[k] = target[j]
            
            # Position decision_pos should be > target[decision_pos]
            k_dec = pos_to_half(decision_pos)
            if k_dec == -1:  # middle
                if middle <= target[decision_pos]:
                    return None
            else:
                if k_dec in constraints:
                    if constraints[k_dec] <= target[decision_pos]:
                        return None
            
            # Check if constraints are satisfiable with available characters
            used = Counter()
            for k in constraints:
                used[constraints[k]] += 1
            for c in used:
                if avail[c] < used[c]:
                    return None
            for c in used:
                avail[c] -= used[c]
            
            # For position decision_pos, if not already constrained, find smallest char > target[decision_pos]
            if k_dec != -1 and k_dec not in constraints:
                found = None
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c > target[decision_pos] and avail[c] > 0:
                        found = c
                        break
                if found is None:
                    return None
                constraints[k_dec] = found
                avail[found] -= 1
            
            # Fill remaining positions with smallest available characters
            remaining = []
            for c in 'abcdefghijklmnopqrstuvwxyz':
                remaining.extend([c] * avail[c])
            
            unconstrained = [k for k in range(half_len) if k not in constraints]
            if len(remaining) != len(unconstrained):
                return None
            
            unconstrained.sort()
            for i, k in enumerate(unconstrained):
                constraints[k] = remaining[i]
            
            # Build first_half
            first_half = [constraints[k] for k in range(half_len)]
            
            # Construct palindrome
            if n % 2 == 1:
                P = first_half + [middle] + first_half[::-1]
            else:
                P = first_half + first_half[::-1]
            
            return ''.join(P)
        
        # Try each decision position
        for decision_pos in range(n):
            result = try_decide_at(decision_pos)
            if result is not None:
                return result
        
        return ""
# @lc code=end