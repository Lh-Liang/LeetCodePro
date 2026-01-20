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
        
        # Check if palindrome is possible
        odd_char = ''
        odd_counts = 0
        for char in count:
            if count[char] % 2 != 0:
                odd_counts += 1
                odd_char = char
        
        if odd_counts > 1:
            return ""
        
        # Prepare counts for the first half
        half_count = Counter()
        for char, c in count.items():
            half_count[char] = c // 2
            
        m = n // 2
        
        # We want to find the longest prefix of target[0...m-1] we can match,
        # then deviate with a larger character.
        # Or, if n is odd, match target[0...m-1] and find a valid middle char.
        
        # To do this correctly, we iterate backwards from the deviation point.
        # The deviation point i is where our result[i] > target[i].
        # We want the largest possible i (longest matching prefix).
        # Range of i is m down to 0 (if n is odd, we check middle at m).
        
        # Precompute availability of prefixes
        # valid_prefix_len is the length of the longest prefix of target's half we can form.
        temp_half = half_count.copy()
        valid_prefix_len = 0
        for i in range(m):
            char = target[i]
            if temp_half[char] > 0:
                temp_half[char] -= 1
                valid_prefix_len += 1
            else:
                break
        
        # Helper to construct result
        def build_result(prefix_len, deviation_char, current_half_counts):
            # Prefix is target[:prefix_len]
            # Deviation is deviation_char at index prefix_len
            # Rest is filled greedily
            
            res_half = list(target[:prefix_len])
            res_half.append(deviation_char)
            
            # Decrement deviation char count
            current_half_counts[deviation_char] -= 1
            
            # Fill remaining m - 1 - prefix_len characters
            sorted_chars = sorted(current_half_counts.keys())
            for char in sorted_chars:
                count = current_half_counts[char]
                res_half.extend([char] * count)
            
            first_half_str = "".join(res_half)
            
            mid_str = odd_char if n % 2 != 0 else ""
            
            return first_half_str + mid_str + first_half_str[::-1]

        # Case 1: n is odd. Try to match full half, then check middle.
        if n % 2 != 0:
            # Can we match target[0...m-1]?
            if valid_prefix_len == m:
                # We have the half. Now we need to check the middle character.
                # The current palindrome would be target[:m] + odd_char + reversed(target[:m])
                # Is this > target? 
                # Since the first half matches target, we compare the rest.
                # constructed: ... + odd_char + reversed(first_half)
                # target:      ... + target[m] + target[m+1...]
                
                # Actually, simpler logic: The first half is fixed to target[:m].
                # The middle char is fixed to odd_char.
                # The second half is fixed to reversed(target[:m]).
                # So there is only ONE permutation that matches the first half target[:m].
                # We just check if it is > target.
                
                cand = target[:m] + odd_char + target[:m][::-1]
                if cand > target:
                    return cand
        else:
             # If n is even, and we match fully, the palindrome is target[:m] + target[:m][::-1]
             if valid_prefix_len == m:
                 cand = target[:m] + target[:m][::-1]
                 if cand > target:
                     return cand

        # Case 2: Deviate at index i (from m-1 down to 0)
        # We need to maintain the counts corresponding to target[:i]
        # We can re-calculate counts or backtrack. Since m is small (<= 150), re-calc is fine or manage state.
        # Let's manage state. We start with counts for the full valid prefix and backtrack.
        
        # Current counts used for the longest valid prefix
        curr_counts = half_count.copy()
        for i in range(valid_prefix_len):
            curr_counts[target[i]] -= 1
            
        # Iterate i from valid_prefix_len down to 0
        # At index i, we try to put char c > target[i]
        # The prefix target[:i] is valid by definition of loop direction.
        # After checking i, we "give back" target[i-1] to counts for the next iteration (i-1).
        
        # Note: valid_prefix_len could be m. We check deviation at m-1, m-2...
        # If valid_prefix_len < m, we can't deviate at valid_prefix_len (because we can't even place target[valid_prefix_len]),
        # but we can try to place something > target[valid_prefix_len] IF we have it.
        # Actually, if we can't match target[i], we MUST deviate at i or earlier.
        # So we start checking at i = valid_prefix_len.
        
        # If valid_prefix_len == m, we already checked the "match all" case above.
        # So we start strictly looking for deviations.
        
        start_i = valid_prefix_len
        # If we matched everything (m), we start deviating at m-1.
        if start_i == m:
            start_i = m - 1
            # We need to restore the count for the char we are about to remove (target[m-1])
            # implicitly handled by the loop structure logic below if we align it right.
            # Let's align: curr_counts matches target[:valid_prefix_len].
            # If we want to deviate at i, we need counts for target[:i].
        
        # Let's adjust curr_counts to represent target[:start_i]
        # If valid_prefix_len == m, curr_counts has consumed all m chars.
        # We want to start loop at m-1. We need to put back target[m-1...start_i-1]?? No.
        # Let's just fix the loop.
        
        # Correct state management:
        # curr_counts currently reflects consumption of target[:valid_prefix_len].
        
        for i in range(start_i, -1, -1):
            # At this index i, we want to place a char > target[i].
            # First, if i < valid_prefix_len, it means we are backtracking, so we must return target[i] to counts.
            if i < valid_prefix_len:
                curr_counts[target[i]] += 1
            
            # Now curr_counts reflects target[:i].
            # Find smallest char in curr_counts > target[i]
            found_char = None
            for char in sorted(curr_counts.keys()):
                if curr_counts[char] > 0 and char > target[i]:
                    found_char = char
                    break
            
            if found_char:
                return build_result(i, found_char, curr_counts)
        
        return ""
# @lc code=end