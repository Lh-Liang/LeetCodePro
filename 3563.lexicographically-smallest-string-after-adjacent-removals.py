#
# @lc app=leetcode id=3563 lang=python3
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        from functools import lru_cache

        def is_consecutive(a, b):
            return abs(ord(a) - ord(b)) == 1 or (a == 'a' and b == 'z') or (a == 'z' and b == 'a')

        @lru_cache(maxsize=None)
        def dfs(curr):
            res = curr
            n = len(curr)
            for i in range(n - 1):
                if is_consecutive(curr[i], curr[i+1]):
                    next_str = curr[:i] + curr[i+2:]
                    candidate = dfs(next_str)
                    if candidate < res:
                        res = candidate
            return res

        return dfs(s)
# @lc code=end