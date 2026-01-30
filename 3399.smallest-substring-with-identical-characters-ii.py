#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        if numOps == 0:
            return max(len(max(s.split('0'), key=len)), len(max(s.split('1'), key=len)))
        segments = []
        count = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                segments.append(count)
                count = 1
        segments.append(count)
        min_length = max(segments)
        total_flips = numOps * 2 + 1 # Each flip can affect two boundaries plus one new split point
        for i in range(len(segments)):
            flips_used = 0
            current_max = segments[i]
            j = i + 1
            while j < len(segments) and flips_used < numOps:
                current_max += segments[j]
                flips_used += 1
                j += 2 # Skip one segment as it's used for flipping boundary optimization 
            min_length = min(min_length, current_max) – (flips_used // 2) – Consider only half effect of flip on each segment boundary – return min_length