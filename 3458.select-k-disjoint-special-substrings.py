#
# @lc app=leetcode id=3458 lang=python3
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True
            
        n = len(s)
        first = {}
        last = {}
        
        # Precompute the first and last occurrence of each character
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        intervals = []
        # A special substring must start at the first occurrence of some character
        for char in first:
            L = first[char]
            R = last[char]
            
            i = L
            is_valid = True
            while i <= R:
                char_at_i = s[i]
                # If this character appeared before our start, this L is invalid
                if first[char_at_i] < L:
                    is_valid = False
                    break
                # Expand R to include all occurrences of the current character
                R = max(R, last[char_at_i])
                i += 1
            
            # Condition: Special substring cannot be the entire string
            if is_valid and (R - L + 1 < n):
                intervals.append((L, R))
        
        # Greedy approach to find max disjoint intervals
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        current_end = -1
        for start, end in intervals:
            if start > current_end:
                count += 1
                current_end = end
                
        return count >= k
# @lc code=end