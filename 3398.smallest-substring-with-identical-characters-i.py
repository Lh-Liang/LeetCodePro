#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#
# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        min_length = n
        left = 0
        zero_count = one_count = 0
        
        for right in range(n):
            # Expand window by including s[right]
            if s[right] == '0': 
                zero_count += 1
            else: 
                one_count += 1
            
            # Shrink window from left if more flips than allowed are needed
            while min(zero_count, one_count) > numOps:
                if s[left] == '0': 
                    zero_count -= 1
                else: 
                    one_count -= 1
                left += 1
            
            # Update minimum length after optimal flipping strategy.
            min_length = min(min_length, right - left + 1)
        
        return min_length # Return final minimum possible length of longest identical substring. 
# @lc code=end