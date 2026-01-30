#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        def can_make(k):
            # Check if we can make all substrings have length at most k
            for ch in ['0','1']:
                left = 0
                flips = 0
                for right in range(n):
                    if s[right] != ch:
                        flips += 1
                    if right - left + 1 > k:
                        if s[left] != ch:
                            flips -= 1
                        left += 1
                    if right - left + 1 == k:
                        if flips <= numOps:
                            return True
            return False
        lo, hi = 1, n
        answer = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                answer = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return answer
# @lc code=end