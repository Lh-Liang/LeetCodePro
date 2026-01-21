#
# @lc app=leetcode id=3399 lang=python3
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        # Pre-calculate blocks of identical characters
        blocks = []
        if n > 0:
            count = 1
            for i in range(1, n):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    blocks.append(count)
                    count = 1
            blocks.append(count)

        def check(L):
            if L == 1:
                # For L=1, the string must become alternating.
                # Option 1: 010101...
                # Option 2: 101010...
                ops1 = 0
                for i in range(n):
                    expected = '0' if i % 2 == 0 else '1'
                    if s[i] != expected:
                        ops1 += 1
                ops2 = n - ops1
                return min(ops1, ops2) <= numOps
            else:
                # For L > 1, use the block formula: sum of floor(len / (L+1))
                total_ops = 0
                for b in blocks:
                    total_ops += b // (L + 1)
                return total_ops <= numOps

        # Binary search for the minimum max length L
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