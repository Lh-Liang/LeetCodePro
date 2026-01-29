#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        def check(k):
            if k == 1:
                # Case k=1: String must be 0101... or 1010...
                flips1 = 0 # Target: 0101...
                flips2 = 0 # Target: 1010...
                for i in range(n):
                    if int(s[i]) != i % 2:
                        flips1 += 1
                    else:
                        flips2 += 1
                return min(flips1, flips2) <= numOps
            
            # Case k > 1: Break segments of length L
            total_flips = 0
            count = 1
            for i in range(1, n):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    total_flips += count // (k + 1)
                    count = 1
            total_flips += count // (k + 1)
            return total_flips <= numOps

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