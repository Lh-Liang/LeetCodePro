#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        def check(k):
            if k == 1:
                # For k=1, the string must be 0101... or 1010...
                cnt1 = 0  # pattern starting with 0
                cnt2 = 0  # pattern starting with 1
                for i in range(n):
                    # Pattern 1: i % 2
                    if int(s[i]) != (i % 2):
                        cnt1 += 1
                    # Pattern 2: (i + 1) % 2
                    if int(s[i]) != ((i + 1) % 2):
                        cnt2 += 1
                return min(cnt1, cnt2) <= numOps
            else:
                # For k >= 2, we can split blocks independently
                flips = 0
                i = 0
                while i < n:
                    j = i
                    while j < n and s[j] == s[i]:
                        j += 1
                    length = j - i
                    flips += length // (k + 1)
                    i = j
                return flips <= numOps

        low = 1
        high = n
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
# @lc code=end