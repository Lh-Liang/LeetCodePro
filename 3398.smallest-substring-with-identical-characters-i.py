#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        if n == 0: return 0
        # Prefix sums for zeros and ones
        prefix_zeros = [0] * (n + 1)
        prefix_ones = [0] * (n + 1)
        for i in range(n):
            prefix_zeros[i+1] = prefix_zeros[i] + (1 if s[i] == '0' else 0)
            prefix_ones[i+1] = prefix_ones[i] + (1 if s[i] == '1' else 0)
        min_length = n
        # Sliding window approach to use flips effectively
        for start in range(n):
            for end in range(start, n):
                zeros_in_window = prefix_zeros[end+1] - prefix_zeros[start]
                ones_in_window = prefix_ones[end+1] - prefix_ones[start]
                flips_needed = min(zeros_in_window, ones_in_window)
                if flips_needed <= numOps:
                    min_length = min(min_length, end - start + 1)
        return min_length
# @lc code=end