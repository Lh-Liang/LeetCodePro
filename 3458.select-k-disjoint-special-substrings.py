#
# @lc app=leetcode id=3458 lang=python3
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0: return True
        
        n = len(s)
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first: first[char] = i
            last[char] = i
            
        intervals = []
        for char in first:
            l, r = first[char], last[char]
            
            valid = True
            i = l
            while i <= r:
                c = s[i]
                if first[c] < l:
                    valid = False
                    break
                r = max(r, last[c])
                i += 1
            
            # A special substring cannot be the entire string
            if valid and not (l == 0 and r == n - 1):
                intervals.append((l, r))
        
        if not intervals: return k <= 0
        
        # Interval Scheduling Maximization: Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = -1
        for l, r in intervals:
            if l > last_end:
                count += 1
                last_end = r
                
        return count >= k
# @lc code=end