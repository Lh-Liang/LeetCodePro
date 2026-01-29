#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def minLongestSubstringLength(s, numOps, charToFlip):
            n = len(s)
            left = 0
            max_length = n
            flip_count = 0
            for right in range(n):
                if s[right] == charToFlip:
                    flip_count += 1
                while flip_count > numOps:
                    if s[left] == charToFlip:
                        flip_count -= 1
                    left += 1
                max_length = min(max_length, right - left + 1)
            return max_length
        # Consider both cases of flipping '0's and '1's and take the minimum result
        min_len_with_flipping_zeros = minLongestSubstringLength(s, numOps, '0')
        min_len_with_flipping_ones = minLongestSubstringLength(s, numOps, '1')
        return min(min_len_with_flipping_zeros, min_len_with_flipping_ones)
# @lc code=end