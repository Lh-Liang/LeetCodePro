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
                # For k=1, the result must be alternating '0101...' or '1010...'
                # Count flips needed for both patterns
                ops0 = 0 # pattern starting with 0
                ops1 = 0 # pattern starting with 1
                for i in range(n):
                    # Expected char for pattern0 at index i is i % 2
                    if int(s[i]) != (i % 2):
                        ops0 += 1
                    else:
                        ops1 += 1
                return min(ops0, ops1) <= numOps
            
            # For k >= 2, we can greedily flip the (k+1)-th character in any block
            total_ops = 0
            count = 1
            for i in range(1, n):
                if s[i] == s[i-1]:
                    count += 1
                else:
                    total_ops += count // (k + 1)
                    count = 1
            total_ops += count // (k + 1)
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