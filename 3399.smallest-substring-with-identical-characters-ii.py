#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        def can_do(k):
            flips = 0
            i = 0
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
        ans = n
        while left <= right:
            mid = (left + right) // 2
            if can_do(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
# @lc code=end