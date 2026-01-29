#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        if numOps >= n - 1:
            return 1  # With enough operations, we can alternate every character.
        
        # Calculate lengths of segments of identical characters
        segments = []
        i = 0
        while i < n:
            start = i
            while i < n and s[i] == s[start]:
                i += 1
            segments.append(i - start)
        
        max_len = max(segments)
        min_max_len = max_len
        
        # Try to minimize max_len using numOps flips at segment boundaries
        for j in range(len(segments) - 1):
            left_segment = segments[j]
            right_segment = segments[j + 1]
            if numOps > 0:
                # Calculate potential adjustments by flipping at this boundary
                total_length_reduction = min(numOps, (left_segment + right_segment - 1) // 2)
                new_max_len = max(left_segment, right_segment) - total_length_reduction
                min_max_len = min(min_max_len, new_max_len)
                numOps -= total_length_reduction
            else:
                break
        
        return min_max_len
# @lc code=end