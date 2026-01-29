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
        first = [-1] * 26
        last = [-1] * 26
        
        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i
            
        intervals = []
        for char_idx in range(26):
            if first[char_idx] == -1:
                continue
            
            L = first[char_idx]
            R = last[char_idx]
            
            possible = True
            curr_R = R
            i = L
            while i <= curr_R:
                c_at_i = ord(s[i]) - ord('a')
                # If a character inside the range appears before our start, 
                # this start cannot form a valid special substring.
                if first[c_at_i] < L:
                    possible = False
                    break
                if last[c_at_i] > curr_R:
                    curr_R = last[c_at_i]
                i += 1
            
            if possible:
                # Constraint: The substring is not the entire string s.
                if not (L == 0 and curr_R == n - 1):
                    intervals.append((L, curr_R))
        
        # Greedy Interval Scheduling to find max disjoint intervals
        # Sorting by end time is the optimal strategy for maximizing count.
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = -1
        for start, end in intervals:
            if start > last_end:
                count += 1
                last_end = end
                
        return count >= k
# @lc code=end