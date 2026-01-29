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
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        intervals = []
        for char in first:
            l, r = first[char], last[char]
            is_valid = True
            i = l
            # Expand the interval to include all occurrences of all characters within it
            while i <= r:
                char_in_range = s[i]
                if first[char_in_range] < l:
                    is_valid = False
                    break
                r = max(r, last[char_in_range])
                i += 1
            
            # Substring cannot be the entire string
            if is_valid and not (l == 0 and r == n - 1):
                intervals.append((l, r))
        
        # Greedy selection of non-overlapping intervals
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        current_end = -1
        for start, end in intervals:
            if start > current_end:
                count += 1
                current_end = end
        
        return count >= k
# @lc code=end