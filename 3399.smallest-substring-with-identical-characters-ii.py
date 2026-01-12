#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        def check(mid):
            if mid == 1:
                # Check alternating patterns 0101... and 1010...
                cnt1 = 0 # pattern starting with 0
                cnt2 = 0 # pattern starting with 1
                for i in range(n):
                    expected1 = '0' if i % 2 == 0 else '1'
                    if s[i] != expected1:
                        cnt1 += 1
                    if s[i] == expected1:
                        cnt2 += 1
                return min(cnt1, cnt2) <= numOps
            
            # For mid >= 2, count flips needed for blocks of identical characters
            total_ops = 0
            count = 1
            for i in range(1, n):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    total_ops += count // (mid + 1)
                    count = 1
            total_ops += count // (mid + 1)
            return total_ops <= numOps

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