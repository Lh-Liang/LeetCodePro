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
        
        # Record first and last occurrences of each character
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        intervals = []
        
        # Try to form a special substring starting with the first occurrence of each character
        for char in first:
            start = first[char]
            end = last[char]
            
            # Expand the interval to include all occurrences of characters inside it
            current = start
            valid = True
            while current <= end:
                c_curr = s[current]
                if first[c_curr] < start:
                    # This character starts before our interval's start,
                    # so this interval cannot be a valid special substring starting at 'start'
                    valid = False
                    break
                end = max(end, last[c_curr])
                current += 1
            
            # Check if the interval is valid and not the entire string
            if valid and not (start == 0 and end == n - 1):
                intervals.append((start, end))
        
        # Interval Scheduling: Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = -1
        
        for start, end in intervals:
            if start > last_end:
                count += 1
                last_end = end
                
        return count >= k

# @lc code=end