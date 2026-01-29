#
# @lc app=leetcode id=3398 lang=python3
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        
        def check(k: int) -> bool:
            if k == 1:
                # For k=1, the string must alternate between 0 and 1.
                # We check two patterns: starting with '0' or starting with '1'.
                cost0 = 0
                cost1 = 0
                for i in range(n):
                    # Pattern 0: 0, 1, 0, 1...
                    target0 = '0' if i % 2 == 0 else '1'
                    if s[i] != target0: cost0 += 1
                    # Pattern 1: 1, 0, 1, 0...
                    target1 = '1' if i % 2 == 0 else '0'
                    if s[i] != target1: cost1 += 1
                return min(cost0, cost1) <= numOps
            
            # For k >= 2, use a greedy approach on contiguous segments.
            ops_needed = 0
            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                length = j - i
                # To break a block of length L into blocks of max length k,
                # we need L // (k + 1) flips.
                ops_needed += length // (k + 1)
                i = j
            return ops_needed <= numOps

        # Binary search for the minimum k in range [1, n].
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