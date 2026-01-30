#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        def can_make(k):
            # Return True if we can make all blocks <= k with numOps flips
            i = 0
            flips = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                length = j - i
                if length > k:
                    flips += (length - 1) // k
                i = j
            return flips <= numOps

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if can_make(mid):
                right = mid
            else:
                left = mid + 1
        return left
# @lc code=end