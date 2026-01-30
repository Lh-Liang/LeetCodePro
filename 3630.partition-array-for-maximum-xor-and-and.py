#
# @lc app=leetcode id=3630 lang=python3
#
# [3630] Partition Array for Maximum XOR and AND
#

# @lc code=start
class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        from functools import lru_cache
        n = len(nums)
        @lru_cache(None)
        def dfs(i, xorA, andB, usedB, xorC):
            if i == n:
                return xorA + (andB if usedB else 0) + xorC
            # Option 1: assign nums[i] to A
            res = dfs(i+1, xorA ^ nums[i], andB, usedB, xorC)
            # Option 2: assign nums[i] to B
            if usedB:
                res = max(res, dfs(i+1, xorA, andB & nums[i], True, xorC))
            else:
                res = max(res, dfs(i+1, xorA, nums[i], True, xorC))
            # Option 3: assign nums[i] to C
            res = max(res, dfs(i+1, xorA, andB, usedB, xorC ^ nums[i]))
            return res
        return dfs(0, 0, 0, False, 0)
# @lc code=end