#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        if numOps == 0:
            # Calculate maximum segment length without any operations
            max_seg_len = 0
            current_len = 1
            for i in range(1, n):
                if s[i] == s[i-1]:
                    current_len += 1
                else:
                    max_seg_len = max(max_seg_len, current_len)
                    current_len = 1
            return max(max_seg_len, current_len)
        
        # Sliding window approach with two pointers
        min_length = n
        left = zero_count = one_count = 0
        for right in range(n):
            if s[right] == '0':
                zero_count += 1
            else:
                one_count += 1
            
            # Adjust left pointer if flips needed exceed numOps
            while min(zero_count, one_count) > numOps:
                if s[left] == '0':
                    zero_count -= 1
                else:
                    one_count -= 1
                left += 1
            
            # Calculate effective length after considering flips within this window
            min_length = min(min_length, right - left + 1)
        
        return min_length # Minimum length after optimal flipping strategy.
n# @lc code=end