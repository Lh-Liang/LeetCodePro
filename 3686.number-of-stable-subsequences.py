#
# @lc app=leetcode id=3686 lang=python3
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        # e1: ends in 1 even, e2: ends in 2 evens
        # o1: ends in 1 odd, o2: ends in 2 odds
        e1, e2, o1, o2 = 0, 0, 0, 0
        
        for x in nums:
            if x % 2 == 0:
                # New subsequences ending in exactly two evens
                # come from those previously ending in exactly one even
                added_e2 = e1
                # New subsequences ending in exactly one even
                # come from those ending in any number of odds, plus the singleton [x]
                added_e1 = (o1 + o2 + 1) % MOD
                
                e1 = (e1 + added_e1) % MOD
                e2 = (e2 + added_e2) % MOD
            else:
                # New subsequences ending in exactly two odds
                added_o2 = o1
                # New subsequences ending in exactly one odd
                added_o1 = (e1 + e2 + 1) % MOD
                
                o1 = (o1 + added_o1) % MOD
                o2 = (o2 + added_o2) % MOD
                
        return (e1 + e2 + o1 + o2) % MOD
# @lc code=end