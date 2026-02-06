#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def canAchieve(max_len):
            count_flips = 0
            zeroes = ones = 0
            left = 0
            for right in range(len(s)):
                if s[right] == '0':
                    zeroes += 1
                else:
                    ones += 1
                while min(zeroes, ones) > numOps:
                    if s[left] == '0':
                        zeroes -= 1
                    else:
                        ones -= 1
                    left += 1
                # Check if current window can be reduced within max_len by applying flips
                if (right - left + 1) - max(zeroes, ones) <= numOps and right - left + 1 <= max_len:
                    return True
            return False
        
        left, right = 1, len(s)
        while left < right:
            mid = (left + right) // 2
            if canAchieve(mid):
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end