#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        def check(L):
            cnt = 0
            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                run_len = j - i
                if run_len > L:
                    cnt += (run_len // (L + 1))
                i = j
            return cnt <= numOps
        left, right = 1, n
        ans = n
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
# @lc code=end