#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#
# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        left = 0
        max_len = n
        num_flips = 0
        max_identical = 0
        # A dictionary to track counts of '0's and '1's in current window
        count = {'0': 0, '1': 0}
        for right in range(n):
            count[s[right]] += 1
            # Update the number of flips needed if we want to change all to either '0' or '1'
            max_identical = max(count['0'], count['1'])
            # Calculate number of flips required to make all characters in current window identical
            num_flips = (right - left + 1) - max_identical
            # If num_flips exceeds numOps, move left pointer forward to reduce window size
            if num_flips > numOps:
                count[s[left]] -= 1
                left += 1
            # Update max_len with minimum found so far
            max_len = min(max_len, right - left + 1)
        return max_len 
# @lc code=end