#
# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        # e0: ends in 1 even, e1: ends in 2 evens
        # o0: ends in 1 odd, o1: ends in 2 odds
        e0, e1, o0, o1 = 0, 0, 0, 0
        
        for x in nums:
            if x % 2 == 0:
                # New e0 can be formed by adding current even to:
                # - empty subsequence (1 way)
                # - any subsequence ending in odd (o0 + o1)
                new_e0 = (1 + o0 + o1) % MOD
                # New e1 can be formed by adding current even to:
                # - any subsequence ending in exactly 1 even (e0)
                new_e1 = e0
                
                e0 = (e0 + new_e0) % MOD
                e1 = (e1 + new_e1) % MOD
            else:
                # New o0 can be formed by adding current odd to:
                # - empty subsequence (1 way)
                # - any subsequence ending in even (e0 + e1)
                new_o0 = (1 + e0 + e1) % MOD
                # New o1 can be formed by adding current odd to:
                # - any subsequence ending in exactly 1 odd (o0)
                new_o1 = o0
                
                o0 = (o0 + new_o0) % MOD
                o1 = (o1 + new_o1) % MOD
                
        return (e0 + e1 + o0 + o1) % MOD
# @lc code=end